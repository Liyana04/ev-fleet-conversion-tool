const menuIcon = document.querySelector('#menu-icon')
const navbar = document.querySelector('#navbar ul')

menuIcon.addEventListener('click',()=>{
  menuIcon.classList.toggle('bx-x');// Toggle the icon
  navbar.classList.toggle('active');// Show or hide the menu
})


// // below this just try and error
// function openCity(evt, tabName) {
//   var i, x, tablinks;
//   x = document.getElementsByClassName("tab");
//   for (i = 0; i < x.length; i++) {
//     x[i].style.display = "none";
//   }
//   tablinks = document.getElementsByClassName("tablink");
//   for (i = 0; i < x.length; i++) {
//     tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
//   }
//   document.getElementById(tabName).style.display = "block";
//   evt.currentTarget.className += " w3-red";
// }



//     // Initialize the tooltip
//     const rangeInput = document.getElementById('customRange1');
//     const tooltip = new bootstrap.Tooltip(rangeInput);

//     // Update tooltip and range value dynamically
//     rangeInput.addEventListener('input', function () {
//       const value = `${rangeInput.value} km/year`;
//       rangeInput.setAttribute('data-bs-original-title', value);
//       tooltip.update(); // Update the tooltip's content
//       document.getElementById('rangeValue').innerText = value; // Update the text below
//     });

 
//     // Initialize all tooltips on the page
//     const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
//     tooltipTriggerList.map(function (tooltipTriggerEl) {
//       return new bootstrap.Tooltip(tooltipTriggerEl);
//     });