document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    axios.post('/add_user', {
        name: formData.get('name'),
        email: formData.get('email')
    })
    .then(function (response) {
        document.getElementById('message').textContent = response.data.message;
        document.getElementById('userForm').reset();
    })
    .catch(function (error) {
        console.error('Error:', error);
    });
});
