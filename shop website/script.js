// კალათში ნივთების დამატება
function addToCart(item) {
    const cartItemsList = document.getElementById('cart-items');
    const cartItem = document.createElement('li');
    cartItem.textContent = item;
    cartItemsList.appendChild(cartItem);
}

// გადახდის გადამისამართება
function checkout() {
    const cartItems = document.getElementById('cart-items').children;
    if (cartItems.length === 0) {
        alert('გთხოვთ, აირჩიოთ პროდუქტი!');
    } else {
        alert('შეკვეთა შესრულდა!');
        document.getElementById('cart-items').innerHTML = '';
    }
}
