const https = require("https");
const app_id = "UADY's App";
const app_key = "80d80f62";
const wordId = "ace";
const fields = "pronunciations";
const strictMatch = "false";

const options = {
   host: 'od-api.oxforddictionaries.com',
   port: '443',
   path: '/api/v2/entries/en-gb/' + wordId + '?fields=' + fields + '&strictMatch=' + strictMatch,
   method: "GET",
   headers: {
     'app_id': app_id,
     'app_key': app_key
   }
 };

https.get(options, (resp) => {
  let body = '';
  resp.on('data', (d) => {
    body += d;
  });
  resp.on('end', () => {
    let parsed = JSON.stringify(body);
    console.log(parsed);
  });
});


let butt = document.getElementById('button');
butt.addEventListener('onclick', function (e) {
   
});




/* <div class="b-send">
    <form id="form-widget">
        <div class="wrp-field">
            <label for="key-word" class="form__label">Enter a word to test the API</label>
            <input id="key-word" class="input-key" type="text" name="" placeholder="Try it out">
            <button id="button" type="button" class="js-send">Send</button>
        </div>
        <span class="slogan" style="display: none;">Enter a word above to see the API in action …</span>
    </form>
</div>

<div class="js-result">
    <div class="left">
        <span class="lexical-cat"></span>
        <span class="part_speech"></span>
        <strong>Definition</strong>
        <span class="def"></span>
        <strong>Example sentence</strong>
        <span class="example"></span>
        <!--<strong>Corpus frequency</strong>-->
        <!--<span class="frequency" style="display: none;">Normalized frequency =&nbsp; <span style="display: inline-block" class="frequency-number"></span></span>-->
    </div>

    <div class="right">
        <a class="btn" href="#plans">GET YOUR API KEY!</a>
    </div>
</div>*/