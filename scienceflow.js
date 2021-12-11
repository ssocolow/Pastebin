// Google apps script code

function onFormSubmit() {
  let form = FormApp.openById('1Gnwa_ROa4WQOIS2xoRT_X10RmeIWtl7Jzk9QX1R9CQY'); //open form
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
  //set the confirmation message - unfortunately only updates it for when the form is requested next, will not change this form
  form.setConfirmationMessage("hi, lksdjf");
  //append the info the spreadsheet
  addRecord(info[0],info[1],info[2]);
  //send email to the person who submitted the form
  sendEmail(email, info);
}

//return string which is the list of reccomended classes
//go through each case and return the reccomendations
function reccomdedClasses(info){
  switch(info[1]){
    case "Honors Earth Science":
      if (info[2] === "A" || "B" || "C") {
        return "Recconemdation is L1 Bio and Honors Bio"
      }
  }
}
//append info to spreadsheet
function addRecord(currentclass, year, grade){
  //get spreadsheet url and open it and then get the first sheet
  let url = 'https://docs.google.com/spreadsheets/d/1B2D15_Rv9_8ZYo_r_2Dc0HIAIzV7Qicnqdh8o3VbTVY/edit#gid=0';
  let ss = SpreadsheetApp.openByUrl(url);
  let dataSheet = ss.getSheetByName("Sheet1");
  //the data to the spreadsheet
  dataSheet.appendRow([currentclass, year, grade, new Date()]);
}

//send email
function sendEmail(addr, info){
  MailApp.sendEmail({
    to: addr,
    subject: "Science Class Reccomendations",
    body: reccomdedClasses(info),
  })
}

