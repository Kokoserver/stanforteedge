const lightbox = document.createElement("div");
lightbox.id = "lightbox";
document.body.appendChild(lightbox);

const images = document.querySelectorAll(".lightbox-img");
images.forEach((image) => {
  image.addEventListener("click", (e) => {
    lightbox.classList.add("active");
    const img = document.createElement("img");
    img.src = image.src;
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild);
    }
    lightbox.appendChild(img);
  });
});

lightbox.addEventListener("click", (e) => {
  if (e.target !== e.currentTarget) return;
  lightbox.classList.remove("active");
});

var clientSwiper = new Swiper(".client-swiper", {
  autoplay: {
    delay: 5000,
  },

  slidesPerView: 3,
  spaceBetween: 10,
  slidesPerGroup: 5,
  // effect: "fade",
  loop: true,
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 3,
      spaceBetween: 10,
    },
    // when window width is >= 640px
    640: {
      slidesPerView: 5,
      spaceBetween: 10,
    },
  },
  loopFillGroupWithBlank: true,
  pagination: {
    el: ".client-pagination",
    clickable: true,
  },
  // navigation: {
  //   nextEl: ".swiper-button-next",
  //   prevEl: ".swiper-button-prev",
  // },
});

var heroSwiper = new Swiper(" .hero-swiper", {
  effect: "cube",
  grabCursor: true,
  cubeEffect: {
    shadow: false,
    slideShadows: false,
    shadowOffset: 0,
    shadowScale: 0,
  },
  autoplay: {
    delay: 6000,
  },

  loopFillGroupWithBlank: true,
  pagination: {
    el: ".hero-pagination",
    clickable: true,
  },
});

var heroSwiper = new Swiper(".project-swiper", {
  autoplay: {
    delay: 10000,
  },
  loop: true,
  slidesPerView: 2,
  slidesPerGroup: 3,

  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    480: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    640: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
  },

  loopFillGroupWithBlank: false,
  pagination: {
    el: ".project-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

var whatWeDoSwpiper = new Swiper(".wwd-swiper", {
  autoplay: {
    delay: 10000,
  },
  slidesPerView: 3,
  spaceBetween: 10,
  slidesPerGroup: 3,
  loop: true,
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    480: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    640: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
  },

  loopFillGroupWithBlank: false,
  pagination: {
    el: ".wwd-pagination",
    clickable: true,
  },
  // navigation: {
  //   nextEl: ".swiper-button-next",
  //   prevEl: ".swiper-button-prev",
  // },
});
