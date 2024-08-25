function loadReports() {
    const reports = JSON.parse(localStorage.getItem('reports')) || []
    reports.forEach((report) => {
        const listItem = document.createElement('li');
        listItem.textContent = `Disaster Type: ${report.disasterType}, Location: ${report.location}, Date: ${report.date}, Description: ${report.description}`;
        document.querySelector("#reportList").appendChild(listItem);
    });
}
// Load reports when the page loads
window.onload = loadReports;