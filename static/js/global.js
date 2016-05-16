/**
 * Created by baptiste on 26/02/16.
 */
$(function(){
   $(".stackMessages .message").each(function(index,element){
      $(element).removeClass("hidden");
       setTimeout(function(){
        $(element).addClass("hidden");
           setTimeout(function(){
               $(element).remove();
           },500)
       },5000);
   });

    var activeHeader = true;

    var $header = $("header");
    $("body").css("padding-top",$header.innerHeight());
    if($(window).width() < 600){
        activeHeader = false;
    }
    $(window).on('resize',function(e){
        $("body").css("padding-top",$header.innerHeight());
        if($(window).width() < 600){
            activeHeader = false;
            $header.css("top",0+"px");
        } else {
            activeHeader = true;
        }
    });

    var lastScroll = $(window).scrollTop();
    $(window).on('scroll',function(e){
        if(activeHeader) {
            var thisScroll = $(window).scrollTop();
            var lastTop = $header.css("top");
            lastTop = parseInt(lastTop.slice(0, lastTop.length - 2));
            var newTop = 0;

            if (thisScroll > lastScroll) {
                newTop = lastTop + (lastScroll - thisScroll);
                if (newTop <= -($header.innerHeight() + 30)) {
                    newTop = -($header.innerHeight() + 30);
                }
            } else if (thisScroll < lastScroll) {
                newTop = lastTop - (thisScroll - lastScroll);
                if(thisScroll < $header.innerHeight()){
                    if (newTop >= 0) {
                        newTop = 0;
                    }
                } else {
                    if (newTop >= -$header.find("h1").innerHeight()) {
                        newTop = -$header.find("h1").innerHeight();
                    }
                }
            }
            lastScroll = thisScroll;
            $header.css("top",newTop+"px");
        }
    });
});