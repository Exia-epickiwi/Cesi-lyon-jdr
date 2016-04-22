$(function(){

    $(".medias .media").each(function(index,element){
        var el = $(element);
        var img = el.find("img").get(0);
        if(img && img.width < img.height){
            el.addClass("reverseDimentions");
        }
    });


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

    $(".medias").on("click",".media:not(.add):not(.tmp)",function(e){
        prompt("Insèrer cette balise pour afficher l'image","$[["+$(this).data("name")+"]]");
    });

    $("#addImage").on("click",function(e){
        $(".medias").toggleClass("blurred");
        $(".verticalButtons").toggleClass("blurred");
        $(".addForm").toggleClass("show");
    });

    $("#cancelUpload").on("click",function(e){
        $(".medias").removeClass("blurred");
        $(".verticalButtons").removeClass("blurred");
        $(".addForm").removeClass("show");
        $("#errorForm").html("");
    });

    $('#uploadForm').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        $("#addImage").before(
"<div class='media add tmp'><div class='image'><i class='material-icons'>file_upload</i></div><div class='info'><span class='name'>Envoie de votre image en cours</span></div></div>");
        $.ajax({
            type:'POST',
            url: $(this).attr('action'),
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                var newMedia = JSON.parse(data);
                $(".medias .media.tmp").remove();
                $("#addImage").before(
"<div class='media' data-name='"+newMedia.name+"'><div class='image'><img src='"+newMedia.fileUrl+"'></div><div class='info'><span class='name'>"+newMedia.name+"</span> <span class='author'>"+newMedia.author+"</span><span class='date'>"+newMedia.date+"</span></div></div>");
        $("#cancelUpload").click();
            },
            error: function(data){
                $(".medias .media.tmp").remove();
                $(".medias").addClass("blurred");
                $(".verticalButtons").addClass("blurred");
                $(".addForm").addClass("show");
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
        $(".medias").removeClass("blurred");
        $(".verticalButtons").removeClass("blurred");
        $(".addForm").removeClass("show");
    }));

    $(window).on("keypress",function(e){
        if(e.keyCode == 13 && e.ctrlKey){
            $("form").submit();
        }
    });
});