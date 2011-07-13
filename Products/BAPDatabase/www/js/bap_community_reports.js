$(document).ready(function(){
	/**
	 * Hide all objectives` content if Javascript Enabled
	 */
	hideItems();
    if(window.location.hash) {
        var hashed = $(normalize_id(window.location.hash));
        hashed.siblings().show();
        hashed.parents().slideDown();        
    }
    $('.bap-objective-title a').click(function(e){
	    e.preventDefault();
    	update_links('/bap');

	    if($(this).parent().next('.bap-objective').is(':visible')){
	        $(this).attr("class", "active");
    	}else {
	        $(this).attr("class", "inactive");
    	}

    	$(this).parent().next('.bap-objective').slideToggle();
    });

	$('.bap-objective-title span').click(function(e){
		update_links('/bap');
		objective_id = $(this).parent().children('a').text();
		toggle_objective($(this));
	});

	$('.bap-objective .bap-targets .bap-target span a.target-link').click(function(){
		update_links('/bap');
		target_id = $(this).attr('href').split('?id=')[1];
		toggle_target($(this));
		return false;
	});

	$('.action-link').click(function(){
		update_links('/bap');
		action_id = $(this).attr('href').split('?id=')[1];
		toggle_action($(this));
		return false;
	});

	$('.goto-action').live('click', function(){
		var href = $(this).attr('href');
		href = normalize_id(href);
        $(href).parents().show();
		toggle_action($(href));
	});

	$('.bap-action span span').each(function(){
		$(this).html(replace_actions($(this).html()));
	});
});


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
	var bap_actions = Target.parent().next('.bap-actions')
	if(bap_actions.children('.bap-action').children('.bap-mop-content').length == 0){
		bap_actions.append("<div class='bap-action'><div class='bap-mop-content'></div></div>");
		
		url = Target.attr("href");
	   
		$("#bap-content").showLoading();
		
		bap_actions.children('.bap-action').children('.bap-mop-content').
            load('' + url + ' #mop-content', function(response, status, xhr) {
			$("#bap-content").hideLoading();
			
			if(status == "error"){
				alert(xhr.status + " " + xhr.statusText);
			}
		});

		bap_actions.slideDown();
		bap_actions.children(".bap-mop-content").slideDown();
	}else {
		bap_actions.slideToggle();
		bap_actions.children(".bap-mop-content").slideToggle();
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
			//Replace Action: A1.2. with <a href=
			$(this).html(replace_actions($(this).html()));
			//Also linkify text
			$(this).html(Linkify($(this).html()));
			if(status == "error"){
				alert(xhr.status + " " + xhr.statusText);
			}
		});
		Action.parent().next(".bap-mop-content").slideDown();
	}else {
		Action.parent().next(".bap-mop-content").slideToggle();
	}
}

function update_links(parameter){
	parameter = parameter || "";
	$('.sub_folder ul li a').each(function(){
		if (parameter!=""){
			old_link = $(this).attr('href').split(parameter);
			$(this).attr('href', old_link[0]+parameter);
		}
	});
}
function normalize_id(text){
    return text.replace(/\./g, '\\.');
}
function replace_actions(html){
	return html.replace(/\b(\w{1})\s*\.?(\d+)\.(\d+)\.(\d+)/g,
		'<a class="goto-action" href="#$1$2.$3.$4">$1$2.$3.$4</a>');
}
