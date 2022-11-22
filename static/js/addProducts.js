var loadFile = function(event) {
    var output = document.getElementById('imgoutput');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };
  
const nameinput = document.getElementById('nameinput');
const nameoutput = document.getElementById('nameoutput');

const inputName = function(e) {
    nameoutput.innerHTML = e.target.value;
}

nameinput.addEventListener('input', inputName);
nameinput.addEventListener('propertychange', inputName);

const priceinput = document.getElementById('priceinput');
const priceoutput = document.getElementById('priceoutput');

const inputPrice = function(e) {
    priceoutput.innerHTML = e.target.value + " €";
}

priceinput.addEventListener('input', inputPrice);
priceinput.addEventListener('propertychange', inputPrice);


const ChangeColor = function() {
    const color1input = document.getElementById('color1input');
    const color2input = document.getElementById('color2input');
    const gradient = document.getElementById('gradient');
    const gradient2 = document.getElementById('gradient2');
    const gradient3 = document.getElementById('gradient3');
    gradient.style.background = 
    "linear-gradient( " 
    + color1input.value 
    + ", " 
    + color2input.value 
    + ")";
    gradient2.style.background = 
    "linear-gradient( " 
    + color1input.value 
    + ", " 
    + color2input.value 
    + ")";
    gradient3.style.background = 
    "linear-gradient( " 
    + color1input.value 
    + ", " 
    + color2input.value 
    + ")";
    
    
}


function shoes(){
    const  shoes =  document.getElementById("shoes").value;
    const  sizeoutput =  document.getElementById("sizeoutput");
    sizeoutput.innerHTML = shoes
}
function clothes(){
    const  clothes =  document.getElementById("clothes").value;
    const  sizeoutput =  document.getElementById("sizeoutput");
    sizeoutput.innerHTML = clothes
}
function sizes() {
    const  c = document.getElementById("category").value;
    const  shoes =  document.getElementById("shoes");
    const  clothes =  document.getElementById("clothes");
    const  accesories =  document.getElementById("accesories");
    
    if (c == "Shoes"){
        console.log("Shoes")
        shoes.style.display = "inline-block"
        clothes.style.display = "none"
        accesories.style.display = "none"
        
        
    }
    else if (c == "Clothes"){
        console.log("clothes")
        clothes.style.display = "inline-block"
        shoes.style.display = "none"
        accesories.style.display = "none"
        
    }
    else if (c == "Accesories"){
        console.log("accesories")
        accesories.style.display = "inline-block"
        shoes.style.display = "none"
        clothes.style.display = "none"
        
    }
    
}
const stripe = Stripe(
    "pk_test_51M6dQHLUoQwS73AdpvDRcFzQEhEjrZNLv6nEKvMINOuQeQBodB1w8IqyDPNcbVlm4IwkdA0dh7BPtGs2t0tA1Mi300R9aNf7kJ"
  );
  const elements = stripe.elements();
  const style = {
    base: {
      // Add your base input styles here. For example:
      fontSize: "16px",
      color: "#32325d",
    },
  };

  // Create an instance of the card Element.
  const card = elements.create("card", { style });

  // Add an instance of the card Element into the `card-element` <div>.
  card.mount("#card-element");
  const form = document.getElementById("payment-form");
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { token, error } = await stripe.createToken(card);

    if (error) {
      // Inform the customer that there was an error.
      const errorElement = document.getElementById("card-errors");
      errorElement.textContent = error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(token);
    }
  });
  const stripeTokenHandler = (token) => {
    // Insert the token ID into the form so it gets submitted to the server
    const form = document.getElementById("payment-form");
    const hiddenInput = document.createElement("input");
    hiddenInput.setAttribute("type", "hidden");
    hiddenInput.setAttribute("name", "stripeToken");
    hiddenInput.setAttribute("value", token.id);
    form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
  };