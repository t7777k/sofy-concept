$=jQuery.noConflict();



jQuery(document).ready(function($) {
	
	// When the button is clicked
    $('#goTopBtn').click(function(){
        // Animate the scroll to the top
        $('html, body').animate({ scrollTop: 0 }, 'slow');
        return false;
    });

    var productSlider = $('.mt-mobile_slider');
	var gallerySlider = $('.mt-gallery_grid');
    var isSliderInitialized = false;
	var isRTL = $('html').attr('lang') === 'ar'; 
    // Check if the device is mobile
    function isMobile() {
        return $(window).width() < 768;  // Adjust this to the breakpoint you consider as mobile
    }

    // Initialize Slick slider
    function initializeSlider() {
        if (!isSliderInitialized && isMobile()) {

			
			gallerySlider.slick({
				rtl: isRTL,
				slidesToShow: 1,
				slidesToScroll: 1,
				arrows: false,
				dots: true,
				autoplay: 1,
                autoplaySpeed: 2000,
			});
			
           productSlider.slick({
				rtl: isRTL,
                slidesToShow: 1,
                slidesToScroll: 1,
				arrows: false,
				dots: true,
			//	adaptiveHeight: true,
                autoplay: 1,
                autoplaySpeed: 2000,
				centerMode: true,
  				centerPadding: '80px',
                // Add more settings as needed
            });
			
			
            isSliderInitialized = true;
        }
    }

    // Destroy the Slick slider
    function destroySlider() {
        if (isSliderInitialized && !isMobile()) {
            gallerySlider.slick('unslick');
			productSlider.slick('unslick');
            isSliderInitialized = false;
        }
    }

    // Detect if the element is in the viewport
    function isInViewport(element) {
        var elementTop = element.offset().top;
        var elementBottom = elementTop + element.outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();

        return elementBottom > viewportTop && elementTop < viewportBottom;
    }

    // Check if the slider is in the viewport on scroll
    $(window).on('scroll resize', function() {
        if (isInViewport(productSlider) || isInViewport(gallerySlider)) {
            initializeSlider();
        } else {
            destroySlider();
        }
    });

    // Initial check when the page loads
    if (isInViewport(gallerySlider) || isInViewport(productSlider)) {
        initializeSlider();
    }


	
	
	
	
	
	
	
	
	// Function to check screen width and initialize/destroy Slick Slider
    function initSlick() {
        var screenWidth = $(window).width();
		var isRTL = $('html').attr('lang') === 'ar' || $('html').attr('lang') === 'he' || $('html').attr('lang') === 'fa'; 

        if (screenWidth <= 767) { // Adjust the breakpoint as needed for mobile devices
            // Initialize Slick Slider
            // 
            $('.mt-gallery_grid').slick({
				rtl: isRTL,
				slidesToShow: 1,
				slidesToScroll: 1,
				arrows: false,
				dots: true,
				autoplay: 1,
                autoplaySpeed: 2000,
			});
			
            $('.mt-mobile_slider').slick({
				rtl: isRTL,
                slidesToShow: 1,
                slidesToScroll: 1,
				arrows: false,
				dots: true,
			//	adaptiveHeight: true,
                autoplay: 1,
                autoplaySpeed: 2000,
				centerMode: true,
  				centerPadding: '80px',
                // Add more settings as needed
            });
        } else {
            if ($('.mt-gallery_grid, .mt-mobile_slider').hasClass('slick-initialized')) {
                $('.mt-gallery_grid, .mt-mobile_slider').slick('unslick'); // Destroy slick on larger screens
            }
        }
    }

    // Check screen width on page load
   // initSlick();

    // Re-check screen width on window resize
   $(window).on('resize', function () {
    //    initSlick();
    });
	
	
	
	$('#mt-register').submit(function(e) {
       e.preventDefault();
		$(this).addClass('processing');
        var full_name 		= $('#full_name').val();
        var email_address 	= $('#email_address').val();
		var mobile_number	= $('#mobile_number').val();
		var message			= $('#message').val();

		
        $.ajax({ 
             data: {action: 'get_registration', full_name:full_name, email_address: email_address, mobile_number: mobile_number, message: message },
             type: 'POST',
             url: ajaxurl,
             success: function(data) {
              //   alert(data); 
                  console.log(data); //should print out the name since you sent it along
              $('#message-box').html(data['register']);
				 $('#mt-register').removeClass('processing');
				 
            }
        });
	
    })
	
})


