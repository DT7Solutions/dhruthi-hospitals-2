var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    effect: "fade",
    loop:true,
    autoplay: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });

// 
  $('.collapse').collapse()

  $('#myCollapsible').collapse({
    toggle: false
  })