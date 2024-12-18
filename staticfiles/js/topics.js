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

/**
 * fetches selected topic and interprets choise as a numeric value
 * links topic to selected topic, if not selected = empty
 * fetches subtopic checkboxes
 * loops through all label elements, if labels has content subtopics and the subtopic selected is 1 / 3 it hides the label
 * loops through subtopiccheckboxes and displays them depending on what topic was selected
*/
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

/**
 * fetches selected topic and interprets choise as a numeric value
 * loops through all label elements, if labels has content equipment available and the subtopic selected is 1 / 3 it hides the label
 * shows equipment available checkboxes if selectedtopic equals 2 or 3
 * if the selected topic equals 2 / 3, displays equipment avaiable label
*/

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



topics.addEventListener("change", () => {
    filterSubtopics();
    toggleEquipmentCheckboxes();
    toggleNutritionFocus();
});


filterSubtopics();
toggleEquipmentCheckboxes();
toggleNutritionFocus();