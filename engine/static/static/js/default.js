	$(document).ready(function() {
       
       var footerHeight = 0,
           footerTop = 0,
           $footer = $(".footer");
           
       function positionFooter() {
       
                footerHeight = $footer.height();
                footerTop = ($(window).scrollTop()+$(window).height()-footerHeight)+"px";
       
               if ( ($("body").height()) < $(window).height()) {
                   $footer.css({
                        position: "absolute"
                   }).css({
                        bottom: '0'
                   });
               } else {
                   $footer.css({
                        position: "relative"
                   });
               }
                $("html").css('width', '100px');
                $(".todo").css('min-width', $(window).width());
                $footer.css('min-width', $(window).width());
               
       }
       positionFooter();

       $(window)
               .scroll(positionFooter)
               .resize(positionFooter);

  $('.home .tab-pane ul li a').click(function(){
    $('#youtube-video').hide();
  });

  $('.modal .close').click(function(){
    $('#youtube-video').show();
  });

  $('.modal-footer .btn').click(function(){
    $('#youtube-video').show();
  });

 //Set menu link as active
   var pathname = window.location.pathname;
   //Set menu link as active
   $('.menu a').each(function(){
       var test = $(this).attr('href');
       if (test == pathname){
           $(this).addClass('active');
       } else if(pathname == ''){
          $('.menu a:first').addClass('active');
       }
   });
});

$(document).keyup(function(e) {
  if (e.keyCode == 27) { $('#youtube-video').show(); }   // esc
});