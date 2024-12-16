const topics = document.getElementById("id_topic");
const sub_topics = document.getElementById("id_subtopics");


const TOPIC_SUBTOPICS_MAPPING = {
    0: [0,1,2,3,4,5],
    1: [6,7,8,9,10,11,12],
    2: [13,14,15,16,17,18],
    3: [19,20,21,22,23,24,25,26],
    4: [],
};

function filterSubtopics(){
    const selectedTopic = parseInt(topics.value, 10);
    const allowedSubtopics = TOPIC_SUBTOPICS_MAPPING[selectedTopic] || [];
    const subtopicCheckboxes = document.querySelectorAll("input[name='subtopics']");    
    subtopicCheckboxes.forEach(checkbox => {
        const subtopicValue = parseInt(checkbox.value, 10);
        if(allowedSubtopics.includes(subtopicValue)){
            checkbox.parentElement.style.display = "";
            checkbox.disabled = false;
        } else {
            checkbox.parentElement.style.display = "none";
            checkbox.disabled = true;
            checkbox.checked = false;
        }
    });
}

topics.addEventListener("change", filterSubtopics);

filterSubtopics();