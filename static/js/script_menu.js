const searchInput = document.querySelector('input');
const cuisines = document.querySelectorAll('.column');
const noResultsFound = document.createElement('p');
noResultsFound.textContent = 'No search results found';
noResultsFound.style.display = 'none';
noResultsFound.style.position = 'fixed';
noResultsFound.style.top = '20%';
noResultsFound.style.left = '50%';
noResultsFound.style.transform = 'translate(-50%, -50%)';
noResultsFound.style.fontFamily = 'Arial, sans-serif';
noResultsFound.style.fontSize = '18px';
noResultsFound.style.textAlign = 'center';
noResultsFound.style.backgroundColor = '#e89a3e';
noResultsFound.style.padding = '10px 20px';
noResultsFound.style.borderRadius = '5px';
noResultsFound.style.boxShadow = '0px 0px 5px rgba(0, 0, 0, 0.2)';
document.body.appendChild(noResultsFound);

searchInput.addEventListener('input', () => {
    const searchQuery = searchInput.value.toLowerCase();
    let resultsFound = false;

    cuisines.forEach(cuisine => {
        const cuisineName = cuisine.querySelector('p').textContent.toLowerCase();

        if (cuisineName.includes(searchQuery)) {
            cuisine.style.display = 'block';
            resultsFound = true;
        } else {
            cuisine.style.display = 'none';
        }
    });

    // Show/hide the "No search results found" message
    if (resultsFound) {
        noResultsFound.style.display = 'none';
    } else {
        noResultsFound.style.display = 'block';
    }
});

