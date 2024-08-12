document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('gameForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const move = document.getElementById('move').value;

        // Simulate form submission or handle via AJAX if needed
        form.submit();
    });
});