/*$(function(){
    moment.locale("fr-FR");
    var $dateField = $("#dateField");

    var eventDate = moment.unix(parseInt($dateField.data("timestamp"))).utcOffset(-60);
    $dateField.after("<div class='absoluteDate'>"+$dateField.html()+"</div>");
    $dateField.html(eventDate.fromNow());
    $dateField.addClass("relative");

    setRelativeDates();
});

function setRelativeDates(){
    var $dateField = $("#dateField");
    var eventDate = moment.unix(parseInt($dateField.data("timestamp"))).utcOffset(-60);
    $dateField.html(eventDate.fromNow());
    $(".relativeDate").each(function(index,element){
        $element = $(element);
        var elementDate = moment.unix(parseInt($element.data("timestamp"))).utcOffset(-60);
        $element.html(elementDate.fromNow());
    })
    setTimeout(setRelativeDates,1000);
}*/