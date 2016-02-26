/**
 * Created by baptiste on 16/02/16.
 */

$(function(){
    setTimeout(function(){
       $(".project").each(function(index,element){
           $(element).find(".bar").css("width",$(element).data("progression")+"%");
           $(element).find(".cursor").css("left",$(element).data("progression")+"%");
       });
    },100);

    $(".tasks").on("mousedown",".cursor",function(){
        var $task = $(this).parent().parent();
        $task.addClass("move");
        $("section").addClass("drag");
    });

    $(document).on("mousemove",function(e){
        var $task = $(".task.move");
       if($task.length > 0){
           var $bar = $task.find(".progressionBar");
           var newProgress = Math.round(((e.clientX - $bar.position().left) * 100) / $bar.outerWidth()) - 10;
           if(newProgress >= 0 && newProgress <= 100){
               $task.data("progression",newProgress);
               $bar.find(".bar").css("width",newProgress+"%");
               $bar.find(".cursor").css("left",newProgress+"%");
               $task.find(".progression").html(newProgress+"%");
           }
       }
    });

    $(document).on("mouseup",function(){
        var $task = $(".task.move");
        if($task.length > 0){
            $task.removeClass("move");
            var id = $task.data("id");
            var progress = $task.data("progression");
            $.ajax("/project/task/"+id+"/setprogression?progress="+progress).done(function(data){
                var result = JSON.parse(data);
                if(result.task){
                    $task.data("progression",result.task.progression);
                    $task.find("h3").html(result.task.name);
                    $task.find(".progression").html(result.task.progression+"%");
                    $task.find(".bar").css("width",result.task.progression+"%");
                    $task.find(".cursor").css("left",result.task.progression+"%");
                }
                if(result.error){
                    pulseClass($task,"error",300);
                    console.error("Error "+result.error+" during modification of task : "+result.description);
                } else {
                    pulseClass($task,"success",300);
                }
            });
        }
        $("section").removeClass("drag");
    });
});

function pulseClass($element,className,duration){
    $element.addClass(className);
    setTimeout(function(){
        $element.removeClass(className);
    },duration);
}