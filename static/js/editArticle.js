$(function(){
    $("#toggleNightMode").on("click",function(e){
        e.preventDefault();
        $("body").toggleClass("night")
    });

    $("#toggleMediaWindow").on("click",function(e){
        e.preventDefault();
        $(".contentWrapper").toggleClass("blurred");
        $(".editedArticle").toggleClass("blurred");
        $(".medias").toggleClass("show");
    });

    $(".medias").on("click",".media:not(.add)",function(e){
        prompt("Copiez le nom de cette image avec Ctrl+C",$(this).data("name"));
    });

    $(window).on("keypress",function(e){
        if(e.keyCode == 13 && e.ctrlKey){
            $("form").submit();
        }
    });
});