$(function(){
  var submenuOpen = false;

  $('#nav_main>ul>li>a.menu').mouseenter(function() {closeAllOpen();});

  $('.has_children').mouseenter(function(){
    closeAllOpen();
    var submenu = $(this).siblings('ul.hidden');
    submenuOpen = true;
    submenu.removeClass("hidden");
    submenu.addClass("submenu");
    //submenu.slideDown(300);
    submenu.mouseleave(function(){
      $(this).addClass("hidden").removeClass("submenu");
      //$(this).slideUp(300);
      submenuOpen = false;
    });
  });

  $('#nav_main').mouseleave(function(){
    if(submenuOpen) {
      closeAllOpen();
    }
  });

  function closeAllOpen() {
    $('.has_children').siblings('ul').addClass("hidden").removeClass("submenu");
      //$('.has_children').siblings('ul').slideUp(300);
      submenuOpen = false;
  }

});
