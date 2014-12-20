$(document).ready(function() {
   $(".slider").each(function () { // обрабатываем каждый слайдер
      var obj = $(this);
      $(obj).append("<div class='nav'></div>");
      $(obj).find("li").each(function () {
         $(obj).find(".nav").append("<span rel='"+$(this).index()+"'></span>"); // добавляем блок навигации
         $(this).addClass("slider"+$(this).index());
      });
      $(obj).find("span").first().addClass("on"); // делаем активным первый элемент меню
   });
});
function sliderJS (obj, sl) { // slider function
   var ul = $(sl).find("ul"); // находим блок
   var bl = $(sl).find("li.slider"+obj); // находим любой из элементов блока
   var step = $(bl).width(); // ширина объекта
   $(ul).animate({marginLeft: "-"+step*obj}, 300); // 300 это скорость перемотки
}

function ttt() { // slider click navigate
   var sl = $(this).closest(".slider"); // находим, в каком блоке был клик
   $(sl).find("span").removeClass("on"); // убираем активный элемент
   $(this).addClass("on"); // делаем активным текущий
   var obj = $(this).attr("rel"); // узнаем его номер
   sliderJS(obj, sl); // слайдим
   return false;
};

$(document).on("click", ".slider .nav span", ttt);
window.setInterval(function(){var n = $(".slider .nav span.on").next();if(n.length==0)n=$(".slider .nav span").first();n.click();},5000);
