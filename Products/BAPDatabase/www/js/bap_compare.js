//$(function() {
//    $('.switch-compare').live('click', function(e){
//        e.preventDefault();
//        if( ($('.compare-select.multiple-select').length)){
//            console.log('s');
//            $('.compare-select.multiple-select').removeAttr('multiple').css({'height': 'auto'}).removeClass('multiple-select').addClass('multiple-select-switched');
//        }else {
//            $('.compare-select.multiple-select-switched')
//            .attr('multiple', 'multiple')
//            .css({'height': '145px'})
//            .removeClass('multiple-select-switched')
//            .addClass('multiple-select');
//        }
//    });
//});

$(function() {
    $('.compare-tabs').each(function(){
        if( !$(this).hasClass('single') ){
            id = $(this).attr('id');

            $('#' + id).tabs({
                ajaxOptions: {
                    error: function( xhr, status, index, anchor ) {
                        $( anchor.hash ).html( "Couldn't load this tab. We'll try to fix this as soon as possible." );
                    }
                }
            });
        }
    });
});

$(function(){
    $("select#ctlCountry").change(function(){
        $("select#ctlObjective option[value='']").attr("selected", "selected");
        $("select#ctlTarget").empty();
        $("select#ctlCmpCountries").empty();
    })
})

$(function(){
    $("select#ctlObjective").change(function(){
        var params = $.param({'objective': $(this).val(), 'country': $("select#ctlCountry").val()}, true);
        $.getJSON("json_get_targets", params, function(j){
            var options = '<option value="">select target' + '<'+'/option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].optionValue + '" title="' + j[i].optionTitle + '">' + j[i].optionDisplay + '<'+'/option>';
            }
            $("select#ctlTarget").html(options);
            $("select#ctlCmpCountries").empty();
        })
    })
})

$(function(){
    $("select#ctlTarget").change(function(){
        var params = $.param({'objective': $("select#ctlObjective").val(), 'target': $(this).val(), 'ref_country': $("select#ctlCountry").val()}, true);
        $.getJSON("json_get_countries_filtered_by_actions", params, function(j){
            var options = '';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].optionValue + '" title="' + j[i].optionTitle + '">' + j[i].optionDisplay + '<'+'/option>';
            }
            $("select#ctlCmpCountries").html(options);
        })
    })
})

$(document).ready(function(){
    cookieAction = getCookie("BAPAction");
    
    if(cookieAction !== 'None'){
        toggle_action(cookieAction, true);
    }
    
    
    $('.action-link').click(function(e){
        e.preventDefault();
        action_id = $(this).parent().next('.bap-mop-content').attr('id');
        toggle_action(action_id);
        return false;
    });

    $('.bap-action-content').each(function(){
        $(this).html(Linkify($(this).html()));
    });

    //Shorten long urls
    $('.linkified').each(function(){
        $(this).html($(this).html().substr(0, 50) + '...');
    });
});

function update_links(parameter){
    parameter = parameter || "";
    $('.sub_folder ul li a').each(function(){
        if (parameter!=""){
            old_link = $(this).attr('href').split(parameter);
            $(this).attr('href', old_link[0]+parameter);
        }
    });
}

function toggle_action(action_id, state){
    if($(".bap-mop-content#" + action_id).is(':empty') == true){
        url = $('.action-link', $(".bap-mop-content#" + action_id)).attr("href");

        $("#center_content").showLoading();

        $(".bap-mop-content#" + action_id).load('' + url + ' #mop-content', function(response, status, xhr) {
            $("#center_content").hideLoading();

            if(status == "error"){
                alert(xhr.status + " " + xhr.statusText);
            }
        });

        setCookie('BAPAction', action_id, 60);
        $(".bap-mop-content#" + action_id).slideDown();
    }else {
        if($(".bap-mop-content#"  + action_id).is(':visible') == true){
            setCookie('BAPAction', 'None', 60);
            $(".bap-mop-content#" + action_id).slideUp();
        }else {
            setCookie('BAPAction', action_id, 60);
            $(".bap-mop-content#" + action_id).slideDown();
        }
    }

    if(state == true){
        setCookie('BAPAction', action_id, 60);
        $(".bap-mop-content#" + action_id).slideDown();
    }

return false;
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
