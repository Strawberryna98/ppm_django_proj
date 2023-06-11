window.onscroll = function() {
    showScrollButton();
  };
  
  function showScrollButton() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      document.getElementById("scrollToTopButton").style.display = "block";
    } else {
      document.getElementById("scrollToTopButton").style.display = "none";
    }
  }
  
  function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
  }
