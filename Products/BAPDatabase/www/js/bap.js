$(document).ready(function(){
    /**
     * Hide all objectives` content if Javascript Enabled
    */
    hideItems();
    
    $('.bap-objective-title a').click(function(e){
		update_links('/bap')
        e.preventDefault();
        
        if($(this).parent().next('.bap-objective').is(':visible')){
            $(this).attr("class", "active");
        }else {
            $(this).attr("class", "inactive");
        }
        
        $(this).parent().next('.bap-objective').slideToggle();
		objective_id = $(this).text();
		setCookie('BAPObjective', objective_id, 1);
		deleteCookie('BAPTarget');
		deleteCookie('BAPAction');
    });
    
    $('.bap-objective-title span').click(function(e){
		update_links('/bap');
		objective_id = $(this).parent().children('a').text();
		setCookie('BAPObjective', objective_id, 1);
		deleteCookie('BAPTarget');
		deleteCookie('BAPAction');
		toggle_objective($(this));
    });
    
    $('.bap-objective .bap-targets .bap-target span a.target-link').click(function(){
		update_links('/bap');
		target_id = $(this).attr('href').split('?id=')[1];
		setCookie('BAPTarget', target_id, 1);
		deleteCookie('BAPObjective');
		deleteCookie('BAPAction');
        toggle_target($(this));
		return false;
    });

	$('.action-link').click(function(){
		update_links('/bap');
		action_id = $(this).attr('href').split('?id=')[1];
		setCookie('BAPAction', action_id, 1);
		deleteCookie('BAPObjective');
		deleteCookie('BAPTarget');
        toggle_action($(this));
        return false;
    });

	var action_id = getCookie('BAPAction');
	if (action_id)
	{
		update_links('/bap');
		var Action = $('.action-link[href$='+action_id+']');
		var Target = Action.parents('.bap-target').find('.target-link');
		var objective = Action.parents('.bap-objectives').find('.bap-objective-title span');
		if (Action.length>0)
		{
			toggle_objective(objective);
			toggle_target(Target);
			toggle_action(Action);
		}
	}
	else{
		var target_id = getCookie('BAPTarget');
		if (target_id)
		{
			update_links('/bap');
			var Target = $('.bap-objective .bap-targets .bap-target span a.target-link[href$='+target_id+']');
			var objective = Target.parents('.bap-objectives').find('.bap-objective-title span');
			if (Target.length>0)
			{
				toggle_objective(objective);
				toggle_target(Target);
			}
		}
		else{
			var objective_id = getCookie('BAPObjective');
			if (objective_id)
			{
				update_links('/bap');
				var objective = $('.bap-objective-title a:contains('+objective_id+'):first')
				if (objective.length>0)
				{
					toggle_objective(objective);
				}
			}
		}
	}
	/**
	 * Hide Objectives` content from BAP content
	 *
	 * @author      Bogdan Tanase       Eau de Web
	 * @returns     boolean             false
	*/
	function hideItems(){
		$(".bap-objective").each(function(){
			$(this).css({'display' : 'none'});
		});
		
		$(".bap-actions").each(function(){
			$(this).css({'display' : 'none'});
		});
		
		return false;
	}
	function toggle_target(Target){
		if(Target.parent().next('.bap-actions').children('.bap-action').children('.bap-mop-content').length == 0){
			Target.parent().next('.bap-actions').append("<div class='bap-action'><div class='bap-mop-content'></div></div>");
			
			url = Target.attr("href");
		   
			$("#bap-content").showLoading();
			
			Target.parent().next('.bap-actions').children('.bap-action').children('.bap-mop-content').load('' + url + ' #mop-content', function(response, status, xhr) {
				$("#bap-content").hideLoading();
				
				if(status == "error"){
					alert(xhr.status + " " + xhr.statusText);
				}
			});

			Target.parent().next('.bap-actions').slideDown();
			Target.parent().next('.bap-actions').children(".bap-mop-content").slideDown();
		}else {
			Target.parent().next('.bap-actions').slideToggle();
			Target.parent().next('.bap-actions').children(".bap-mop-content").slideToggle();
	   }
	}

	function toggle_objective(objective){
		if(objective.parent().next('.bap-objective').is(':visible')){
			objective.parent().children('.bap-objective-title a').attr("class", "active");
		}else {
			objective.parent().children('.bap-objective-title a').attr("class", "inactive");
		}
		
		objective.parent().next('.bap-objective').slideToggle();
	}

	function toggle_action(Action){
		if(Action.parent().next(".bap-mop-content").is(':empty') == true){
			url = Action.attr("href");
			
			$("#bap-content").showLoading();
			
			Action.parent().next(".bap-mop-content").load('' + url + ' #mop-content', function(response, status, xhr) {
				$("#bap-content").hideLoading();
				
				if(status == "error"){
					alert(xhr.status + " " + xhr.statusText);
				}
			});
			
			Action.parent().next(".bap-mop-content").slideDown();
		}else {
			Action.parent().next(".bap-mop-content").slideToggle();
		}
	}

	function setCookie(c_name,value,expires){
		// set time, it's in milliseconds
		var today = new Date();
		today.setTime( today.getTime() );
		if ( expires ){
			expires = expires * 1000 * 60 * 60 * 24;
		}
		var expires_date = new Date( today.getTime() + (expires) );
		var path = '/';
		document.cookie=c_name + "=" + escape(value) +
			( ( expires ) ? ";expires=" + expires_date.toGMTString() : "" ) +
			( ( path ) ? ";path=" + path : "" );
	}

	function getCookie(c_name){
		var i,x,y,ARRcookies=document.cookie.split(";");
		for (i=0;i<ARRcookies.length;i++){
			x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
			y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
			x=x.replace(/^\s+|\s+$/g,"");
			if (x==c_name){
				return unescape(y);
			}
		}
	}

	function deleteCookie(name){
		path = '/'
		document.cookie = name + "=" +
			( ( path ) ? ";path=" + path : "") +
			";expires=Thu, 01-Jan-1970 00:00:01 GMT";
	}

	function update_links(parameter){
		$('.sub_folder ul li a').each(function(){
			old_link = $(this).attr('href').split(parameter);
			if (parameter!=''){
				$(this).attr('href', old_link[0]+parameter);
			}
			else{
				$(this).attr('href', old_link[0]);
			}
		});
	}
});
