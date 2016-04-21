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

    $("#addImage").on("click",function(e){
        $(".medias").toggleClass("blurred");
        $(".verticalButtons").toggleClass("blurred");
        $(".addForm").toggleClass("show");
    });

    $("#cancelUpload").on("click",function(e){
        $(".medias").toggleClass("blurred");
        $(".verticalButtons").toggleClass("blurred");
        $(".addForm").toggleClass("show");
        $("#errorForm").html("");
    });

    $('#uploadForm').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type:'POST',
            url: $(this).attr('action'),
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                var newMedia = JSON.parse(data);
                $("#addImage").before(
"<div class='media' data-name='"+newMedia.name+"'><div class='image'><img src='"+newMedia.fileUrl+"'></div><div class='info'><span class='name'>"+newMedia.name+"</span> <span class='author'>"+newMedia.author+"</span><span class='date'>"+newMedia.date+"</span></div></div>")
            $("#cancelUpload").click();
            },
            error: function(data){
                console.log(data);
                var html = "";
                if(data.status == 400){
                    var errors = JSON.parse(data.responseText);
                    console.log(errors);
                    if(errors.name && errors.name[0].code == "unique"){
                        html += "Le nom de l'image n'est pas unique<br/>";
                    }
                    if(errors.file && errors.file[0].code == "invalid_image"){
                        html += "Le fichier donné n'est pas une image<br/>";
                    }
                } else if(data.status == 404) {
                    html = "Une erreur est survenue, assurez vous d'être connecte.";
                } else {
                    html = "Une erreur interne est survenue, reesayez plus tard.";
                }
                $("#errorForm").html(html);
            }
        });
    }));

    $(window).on("keypress",function(e){
        if(e.keyCode == 13 && e.ctrlKey){
            $("form").submit();
        }
    });
});