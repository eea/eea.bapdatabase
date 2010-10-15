$(document).ready(function(){
    /**
     * Hide all objectives` content if Javascript Enabled
    */
    hideItems();
    
    $('.bap-objective-title a').click(function(e){
        e.preventDefault();
        
        if($(this).parent().next('.bap-objective').is(':visible')){
            $(this).attr("class", "active");
        }else {
            $(this).attr("class", "inactive");
        }
        
        $(this).parent().next('.bap-objective').slideToggle();
    });
    
    $('.bap-objective-title span').click(function(e){
        if($(this).parent().next('.bap-objective').is(':visible')){
            $(this).parent().children('.bap-objective-title a').attr("class", "active");
        }else {
            $(this).parent().children('.bap-objective-title a').attr("class", "inactive");
        }
        
        $(this).parent().next('.bap-objective').slideToggle();
    });
    
    $('.bap-objective .bap-targets .bap-target span a.target-link').click(function(){
        if($(this).parent().next('.bap-actions').children('.bap-action').children('.bap-mop-content').length == 0){
            $(this).parent().next('.bap-actions').append("<div class='bap-action'><div class='bap-mop-content'></div></div>");
            
            url = $(this).attr("href");
           
            $("#bap-content").showLoading();
            
            $(this).parent().next('.bap-actions').children('.bap-action').children('.bap-mop-content').load('' + url + ' #mop-content', function(response, status, xhr) {
                $("#bap-content").hideLoading();
                
                if(status == "error"){
                    alert(xhr.status + " " + xhr.statusText);
                }
            });
            
            $(this).parent().next('.bap-actions').slideDown();
            $(this).parent().next('.bap-actions').children(".bap-mop-content").slideDown();
        }else {
            $(this).parent().next('.bap-actions').slideToggle();
            $(this).parent().next('.bap-actions').children(".bap-mop-content").slideToggle();
        }
        
        return false;
    });
    
    $('.action-link').click(function(){
        if($(this).parent().next(".bap-mop-content").is(':empty') == true){
            url = $(this).attr("href");
            
            $("#bap-content").showLoading();
            
            $(this).parent().next(".bap-mop-content").load('' + url + ' #mop-content', function(response, status, xhr) {
                $("#bap-content").hideLoading();
                
                if(status == "error"){
                    alert(xhr.status + " " + xhr.statusText);
                }
            });
            
            $(this).parent().next(".bap-mop-content").slideDown();
        }else {
            $(this).parent().next(".bap-mop-content").slideToggle();
        }
        
        return false;
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