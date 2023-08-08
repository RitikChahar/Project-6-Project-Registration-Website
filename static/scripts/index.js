let storedUID;
let userName;
const baseUrl = "http://127.0.0.1:8000/";

function submitFormToAPI(event) {
  event.preventDefault(); 
  const loader = document.getElementById("resume-loader");
  loader.style.display = "inline-block";
  const resume_form = document.getElementById("form-container-3");
  const section = document.getElementById("section").value;
  const contactNumber = document.getElementById("contactNumber").value;
  const email = document.getElementById("email").value;
  const introduction = document.getElementById("introduction").value;
  const whyWorkWithUs = document.getElementById("whyWorkWithUs").value;
  const resumeFile = document.getElementById("resume").value;
  const uid = document.getElementById("uid").value;
  const payload = {
    section: section,
    contactNumber: contactNumber,
    email: email,
    introduction: introduction,
    whyWorkWithUs: whyWorkWithUs,
    resumeFile: resumeFile,
    uid: uid
  };
  const apiUrl = `${baseUrl}upload-resume/`; 
  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
  .then(response => response.json())
  .then(data => {
      loader.style.display = "none";
      resume_form.classList.add('fade-out');
      resume_form.parentNode.removeChild(resume_form);

      var targetDiv = document.getElementById('form-container-4');
      var newContentContainer = document.createElement('div');
      newContentContainer.innerHTML = `
    <h2 class="thanking-message">Congratulations, You are Successfully Registered!</h2>
`;
      targetDiv.style.visibility = "visible";
      targetDiv.appendChild(newContentContainer);
  })
  .catch(error => {
      loader.style.display = "none";
  });
}

function handleOTPSubmission(event) {
  event.preventDefault();
  const loader = document.getElementById("otp-loader");
  loader.style.display = "inline-block";
  const otpValues = Array.from(document.querySelectorAll('.otp-input')).map(input => input.value);
  const otp = otpValues.join('');

  const otp_form = document.getElementById("form-container-2");
  const resume_form = document.getElementById("form-container-3");
  const footer = document.getElementById("footer");

  const payload = {
    uid: storedUid,
    otp: parseInt(otp)
  };
  fetch(`${baseUrl}verify-otp/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      loader.style.display = "none";
      if (data["status"] == true) {
        otp_form.classList.add('fade-out');
        otp_form.parentNode.removeChild(otp_form);

        var targetDiv = document.getElementById('form-container-3');

        var newContentContainer = document.createElement('div');

        newContentContainer.innerHTML = `
        <form id="resume-form" class="form-resume">
        <h2 class="otp-heading" id="otp-heading">Hey ${userName}, Kindly fill all the details! </h2>
            <label for="uid">UID</label>
            <input type="text" id="uid" name="uid" required>
            <label for="section/Group">Section</label>
            <input type="text" id="section" name="section" required>
            <label for="contactNumber">Contact Number</label>
            <input type="tel" id="contactNumber" name="contactNumber" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
            <label for="email">Personal Email</label>
            <input type="email" id="email" name="email" required>
            <label for="resume">Resume Link</label>
            <input type="text" id="resume" name="resume" required>
            <label for="introduction">Introduction</label>
            <textarea id="introduction" name="introduction" rows="4" cols="50" required></textarea>
            <label for="whyWorkWithUs">Why do you want to work with us?</label>
            <textarea id="whyWorkWithUs" name="whyWorkWithUs" rows="4" cols="50" required></textarea>
            <button type="submit" class="submit-btn"  onclick="submitFormToAPI(event)">Submit</button>
            <span class="loader" id="resume-loader"></span>
        </form>
`;
        footer.style.display = 'none';
        resume_form.style.visibility = "visible";
        targetDiv.appendChild(newContentContainer);
      } else {
        alert("OTP is Incorrect!");

      }
    })
    .catch((error) => {
      loader.style.display = "none";
    });
}

function submitForm(event) {
  const loader = document.getElementById("loader");
  event.preventDefault();

  loader.style.display = "inline-block";
  const name = document.getElementById("name").value;
  const uid = document.getElementById("uid").value;
  const uid_form = document.getElementById("form-container-1");
  const otp_form = document.getElementById("form-container-2");
  const payload = {
    name: name,
    uid: uid,
  };

  fetch(`${baseUrl}register/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      loader.style.display = "none";
      if (data["status"] == false) {
        loader.style.display = "none";
        alert("You are already registered!");
      } else {
        storedUid = uid;
        userName = name;
        uid_form.classList.add('fade-out');
        uid_form.parentNode.removeChild(uid_form);

        var targetDiv = document.getElementById('form-container-2');

        var newContentContainer = document.createElement('div');

        newContentContainer.innerHTML = `
    <span class="loader" id="otp-loader"></span>
    <h2 class="otp-heading" id="otp-heading">Enter the 6-Digit OTP sent to ${uid}@cuchd.in</h2>
    <form id="otp-form">
        <div class="otp-container" id="otp-container">
            <input id="otp-1" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="1" required
                onkeyup="movetoNext(this, 'otp-2')">
            <input id="otp-2" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="2" required
                onkeyup="movetoNext(this, 'otp-3')">
            <input id="otp-3" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="3" required
                onkeyup="movetoNext(this, 'otp-4')">
            <input id="otp-4" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="4" required
                onkeyup="movetoNext(this, 'otp-5')">
            <input id="otp-5" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="5" required
                onkeyup="movetoNext(this, 'otp-6')">
            <input id="otp-6" type="text" class="otp-input" maxlength="1" pattern="[0-9]" name="6" required>
        </div>
        <button type="submit" class="submit-btn"  onclick="handleOTPSubmission(event)">Submit</button>
    </form>
`;
        otp_form.style.visibility = "visible";
        targetDiv.appendChild(newContentContainer);
      }
    })
    .catch((error) => {
      loader.style.display = "none";
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("uid-form");
  form.addEventListener("submit", submitForm);
});

function movetoNext(current, nextFieldID) {
  if (current.value.length >= current.maxLength) {
    document.getElementById(nextFieldID).focus();
  }
}

$(window).on("load", function (){
  $(".loading").fadeOut(2000);
} );