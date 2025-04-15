async function fetchData() {
    const response = await fetch("statics/cleaned_alzheimers_disease_data.json");
    const data = await response.json();
    return data;
  }
  
  function getAgeRange(age) {
    if (age < 65) return "<65";
    if (age < 70) return "65-69";
    if (age < 75) return "70-74";
    if (age < 80) return "75-79";
    if (age < 85) return "80-84";
    return "85+";
  }
  
  function groupByAgeAndField(data, field) {
    const grouped = {};
    data.forEach(item => {
      const ageRange = getAgeRange(item.Age);
      const category = item[field] || "Unknown";
      if (!grouped[ageRange]) grouped[ageRange] = {};
      if (!grouped[ageRange][category]) grouped[ageRange][category] = 0;
      grouped[ageRange][category]++;
    });
    return grouped;
  }
  
  function createStackedBarChart(canvasId, groupedData, title) {
    const labels = Object.keys(groupedData).sort();
    const categories = new Set();
  
    labels.forEach(label => {
      Object.keys(groupedData[label]).forEach(category => categories.add(category));
    });
  
    const datasets = [...categories].map(category => ({
      label: category,
      data: labels.map(label => groupedData[label][category] || 0),
      backgroundColor: `hsl(${Math.random() * 360}, 60%, 60%)`,
    }));
  
    new Chart(document.getElementById(canvasId), {
      type: "bar",
      data: { labels, datasets },
      options: {
        responsive: true,
        
        plugins: {
          title: {
            display: false,
            text: title,
          },
        },
        scales: {
          x: { stacked: true },
          y: { stacked: true, beginAtZero: true }
        }
      }
    });
  }
  
  fetchData().then(data => {
    const ethnicityData = groupByAgeAndField(data, "Ethnicity");
    createStackedBarChart("ethnicityChart", ethnicityData, "Ethnicity by Age");
  
    const genderData = groupByAgeAndField(data, "Gender");
    createStackedBarChart("genderChart", genderData, "Gender by Age");
  }).catch(err => {
    console.error("Error loading JSON data:", err);
  });