document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('vegetableForm');
  const areaSelect = document.getElementById('area');
  const nameSelect = document.getElementById('name');
  const dateInput = document.getElementById('date');
  const today = new Date().toISOString().split('T')[0];
  dateInput.value = today;
  // Fetch the list of areas and populate the select element
  fetch('http://127.0.0.1:5001/areas')
    .then((response) => response.json())
    .then((data) => {
      // Assuming data is an array of area objects with 'id' and 'name' properties
      data.forEach((area) => {
        const option = document.createElement('option');
        option.value = area.id;
        option.textContent = area.name;
        areaSelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error('Error fetching areas:', error);
    });

  fetch('http://127.0.0.1:5001/vegetable_infos')
    .then((response) => response.json())
    .then((data) => {
      data = data.sort((a, b) => {
        if (a.name < b.name) {
          return -1;
        }
      });
      // Assuming data is an array of area objects with 'id' and 'name' properties
      data.forEach((name) => {
        const option = document.createElement('option');
        option.value = name.name;
        option.textContent = name.name;
        nameSelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error('Error fetching areas:', error);
    });

  form.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(form);

    const formDataJson = {};
    formData.forEach((value, key) => {
      formDataJson[key] = value;
    });

    formDataJson.sowed = true;
    formDataJson.planted = false;

    // Send the form data as JSON to the server using AJAX
    fetch('http://127.0.0.1:5001/vegetable_manager', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formDataJson),
    })
      .then((response) => {
        console.log('Response Status:', response.status); // Log the response status

        if (response.status === 201) {
          alert('Vegetable created successfully!');
          // form.reset(); // Clear the form
        } else {
          alert('Error creating vegetable. Please try again.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred while creating the vegetable.');
      });
  });
});
