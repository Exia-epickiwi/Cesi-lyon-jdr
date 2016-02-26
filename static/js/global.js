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
});