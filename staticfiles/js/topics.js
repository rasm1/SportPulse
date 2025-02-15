const form = document.querySelector("form");
const topics = document.getElementById("id_topic");
const sub_topics = document.getElementById("id_subtopics");
const experience_level = document.getElementById("id_experience_level");
const goal = document.getElementById("id_goal");
const workout_frequency = document.getElementById("id_workout_frequency");
const equipment_available = document.getElementById("id_equipment_available");
const nutrition_focus = document.getElementById("id_nutrition_focus");


const TOPIC_SUBTOPICS_MAPPING = {
    0: [0, 1, 2, 3, 4, 5],
    1: [6, 7, 8, 9, 10, 11, 12],
    2: [13, 14, 15, 16, 17, 18],
    3: [19, 20, 21, 22, 23, 24, 25, 26],
    4: [],
};


function filterSubtopics() {
    const selectedTopic = parseInt(topics.value, 10);
    const allowedSubtopics = TOPIC_SUBTOPICS_MAPPING[selectedTopic] || [];
    const subtopicCheckboxes = document.querySelectorAll("input[name='subtopics']");
    document.querySelectorAll('label').forEach(function (label) {
        if (label.textContent === "Subtopics:") {
            label.style.display = selectedTopic === 0 || selectedTopic === 1 || selectedTopic === 2 || selectedTopic === 3 ? "block" : "none";
        }
    });
    subtopicCheckboxes.forEach(checkbox => {
        const subtopicValue = parseInt(checkbox.value, 10);
        if (allowedSubtopics.includes(subtopicValue)) {
            checkbox.parentElement.style.display = "";
            checkbox.disabled = false;
        } else {
            checkbox.parentElement.style.display = "none";
            checkbox.disabled = true;
            checkbox.checked = false;
        }
    });
}


function toggleEquipmentCheckboxes() {
    const selectedTopic = parseInt(topics.value, 10);
    document.querySelectorAll('label').forEach(function (label) {
        if (label.textContent === "Equipment available:") {
            label.style.display = selectedTopic === 2 || selectedTopic === 3 ? "block" : "none";
        }
    });

    if (selectedTopic === 2 || selectedTopic === 3) {
        equipment_available.style.display = 'block';
        equipment_available.disabled = false;
    } else {
        equipment_available.style.display = 'none';
        equipment_available.disabled = true;
    }
}

function toggleNutritionFocus() {
    const selectedTopic = parseInt(topics.value, 10);
    
    document.querySelectorAll('label').forEach(function (label) {
        if (label.textContent === "Nutrition focus:") {
            label.style.display = selectedTopic === 1 ? "block" : "none";
        }
    });

    if (selectedTopic === 1) {
        nutrition_focus.style.display = 'block';  
        nutrition_focus.disabled = false;  
    } else {
        nutrition_focus.style.display = 'none';  
        nutrition_focus.disabled = true;  
    }
}


form.addEventListener("submit", function (event) {
    let value = parseInt(workout_frequency.value, 10);

    if (isNaN(value) || value < 0 || value > 7) {
        alert("Please enter a valid workout frequency between 0 and 7.");
        workout_frequency.focus();
        event.preventDefault(); 
    }
});



topics.addEventListener("change", () => {
    filterSubtopics();
    toggleEquipmentCheckboxes();
    toggleNutritionFocus();
});


filterSubtopics();
toggleEquipmentCheckboxes();
toggleNutritionFocus();