    // Initialize the tooltip
    const rangeInput = document.getElementById('customRange1');
    const tooltip = new bootstrap.Tooltip(rangeInput);

    // Update tooltip and range value dynamically
    rangeInput.addEventListener('input', function () {
      const value = `${rangeInput.value} km/year`;
      rangeInput.setAttribute('data-bs-original-title', value);
      tooltip.update(); // Update the tooltip's content
      document.getElementById('rangeValue').innerText = value; // Update the text below
    });

 
    // Initialize all tooltips on the page
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });