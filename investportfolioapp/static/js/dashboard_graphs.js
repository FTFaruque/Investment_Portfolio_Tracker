// Problem: Graphs are not rendered the first time 


let CHART_INSTANCE = {
    amountChart: null,
    countChart: null
}

document.addEventListener('DOMContentLoaded', function() {

    const selected_category = JSON.parse(document.getElementById("selectedCategory").textContent);
    const labelData = JSON.parse(document.getElementById("labelData").textContent);
    const amountData = JSON.parse(document.getElementById("amountData").textContent);
    const currencyLabel = JSON.parse(document.getElementById("currencyLabel").textContent);
    const currencyFrequency = JSON.parse(document.getElementById("currencyFrequency").textContent);

    chartTitle = `Amount Per Investment In ${selected_category}`;
    if (selected_category == "All"){
        chartTitle = "Investmet Amount Across All Categories"
    }    
    renderGraph(CHART_INSTANCE, "amountChart", labelData, amountData, "amountsChart", chartTitle);

    // INITIAL DISPLAY
    // graphType.EvenListener only works when there is a CHANGE in the drop down menu called "View count by". This means
    // when the page is first loaded, there is no change... it just loaded. So, the graphs are not rendered. The immediate code
    // below is for rendering the graph for the FIRST TIME after the page has loaded. 
    if (selected_category == "All"){
        const categoryFrequency = JSON.parse(document.getElementById("categoryFrequency").textContent);
        renderGraph(CHART_INSTANCE, "countChart", labelData, categoryFrequency, "countsChart", "Number of Investments per Category");
    } else if (selected_category != "All"){
        renderGraph(CHART_INSTANCE, "countChart", currencyLabel, currencyFrequency, "countsChart", "Number of Investments per Currency")
    }

    function updateGraph(graphType){
        console.log("graphType:", graphType);
        if (graphType == "category"){
            const categoryFrequency = JSON.parse(document.getElementById("categoryFrequency").textContent);
            renderGraph(CHART_INSTANCE, "countChart", labelData, categoryFrequency, "countsChart", "Number of Investments per Category");
        } else{
            renderGraph(CHART_INSTANCE, "countChart", currencyLabel, currencyFrequency, "countsChart", "Number of Investments per Currency");
        }
    }
    
    const graphType = document.getElementById("graphType");
    graphType.addEventListener('change', function(e){
        updateGraph(e.target.value);
    })
})



function renderGraph(chartInstance, attribute, label, data, canvasID, title){
    if (chartInstance[attribute]) chartInstance[attribute].destroy();

    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'bottom'
            }
        }
    };

    
    color = (label == '["Empty"] ')? "#808080" : ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
    const amountCtx = document.getElementById(canvasID).getContext('2d');
    chartInstance[attribute] = new Chart(amountCtx, {
        type: 'pie',
        data: {
            labels: label,
            datasets: [{
                data: data,
                backgroundColor: color
            }]
        },
        options: {
            responsive: true,
            cutout: "60%",
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: title
                }
            }
        }
    }); 
}