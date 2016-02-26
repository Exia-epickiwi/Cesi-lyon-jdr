/**
 * Created by baptiste on 11/02/16.
 */
$(function(){
    var titlesSelector = "section .content h1, section .content h2, section .content h3, section .content h4";
    var titles = $(titlesSelector);
    for(var i = 0; i<titles.length; i++){
        var hierarchyIndex = parseInt(titles[i].localName.replace(/.*h([0-9]+).*/i,"$1"))-1;
        $(titles[i]).attr("id","title-"+i);
        var html = "<h"+(hierarchyIndex+1)+"><a href='#title-"+i+"'>"+titles[i].innerHTML+"</a></h"+(hierarchyIndex+1)+">";
        $("#summaryWiki").append(html);
    }

    $(window).on("scroll",function(e){
        if($(window).scrollTop() > $("#summaryWikiWrapper").position().top + 75){
            $("#summaryWiki").css("top",$(window).scrollTop() - $("#summaryWikiWrapper").position().top - 75);
        } else {
            $("#summaryWiki").css("top",0);
        }
    });

    $("#newMessage").on("click",function(e){
        e.preventDefault();
        $("#newMessage").toggleClass("showing");
        $("#newMessageForm").toggleClass("hidden");
    });

    $("#expendMessages").on("click",function(e){
        e.preventDefault();
        $(".comments").toggleClass("expended");
        $("#expendMessages").toggleClass("reverse");
        $("#contentContainer").toggleClass("reduced");
    })
});