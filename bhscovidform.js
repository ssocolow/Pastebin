// Google apps script code

function onFormSubmit() {
  let form = FormApp.openById('1j2KM8WCjKomt9zG7vVssxMR306f6ShVh6ESZLtC3uPg'); //open form
  let formResponses = form.getResponses(); //get all form responses
  let formCount = formResponses.length; //get length of form responses
 
  let info = []; //make info array
 
 
  let intemResponses = formResponses[formCount - 1].getItemResponses(); //get item responses
  let email = formResponses[formCount - 1].getRespondentEmail(); //get the person who submitted the form's email
  //loop over all multiple choices
  for(let i = 0; i < intemResponses.length; i++){
    let r = intemResponses[i];
    let title = r.getItem().getTitle();
    let a = r.getResponse(); //get the choice selected

    info.push(a) //and add that choice to the array
  }
  //send email to the person who submitted the form
  sendEmail(email, info);
}

//return string which is the list of reccomended classes
//go through each case and return the reccomendations
function reccomdedClasses(info){
  switch(info[0]){
    case "Yes":
      if(info[1] == "Blue"){
        return "You should quarantine for not super long because you are vaccinated, and you should watch oceans because you picked blue";
      }
      if(info[1] == "Green"){
        return "You should quarantine for not super long because you are vaccinated, and you should watch grass because you picked green";
      }
    case "No":
      if(info[1] == "Blue"){
        return "You should quarantine for a while because you are not vaccinated, and you should watch oceans because you picked blue";
      }
      if(info[1] == "Green"){
        return "You should quarantine for a while because you are not vaccinated, and you should watch grass because you picked green";
      }
    case "Prefer not to say":
      if(info[1] == "Blue"){
        return "You should quarantine for a while because you did not say, and you should watch oceans because you picked blue";
      }
      if(info[1] == "Green"){
        return "You should quarantine for a while because you did not say, and you should watch grass because you picked green";
      }  
  }
}


//send email
function sendEmail(addr, info){
  MailApp.sendEmail({
    to: addr,
    subject: "Covid Health Reccomendation",
    body: reccomdedClasses(info),
  })
}
