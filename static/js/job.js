function initJobSelector(jobMap) {
    const jobTypeSelect = document.getElementById("jobType");
    const jobLevelSelect = document.getElementById("jobLevel");

    function updateLevels() {
        const selectedJob = jobTypeSelect.value;

        const levels = jobMap[selectedJob] || [];  // 🔥 FIX

        jobLevelSelect.innerHTML = "";

        if (levels.length === 0) {
            const option = document.createElement("option");
            option.textContent = "No levels available";
            jobLevelSelect.appendChild(option);
            return;
        }

        levels.forEach(level => {
            const option = document.createElement("option");
            option.value = level;
            option.textContent = level;
            jobLevelSelect.appendChild(option);
        });
    }

    jobTypeSelect.addEventListener("change", updateLevels);

    updateLevels();
}