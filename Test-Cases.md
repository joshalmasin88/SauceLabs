# Test Cases

### 

### Test Case 1: Add Product And Checkout

**Objective:** To validate the end-to-end process of adding a product to the cart, proceeding to checkout, and completing the order.

Precondition:

1. The website/application is accessible.
2. The user has valid login credentials for the application.

**Test Data:**

* Username: standard\_user
* Password: [password]
* Product: "Sauce Labs Backpack"

Test Steps:

1. Launch the browser and navigate to the URL '[https://www.saucedemo.com/](https://www.saucedemo.com/)'.
2. Enter the username as "standard\_user".
3. Enter the password.
4. Click the "Login" button.
5. Navigate to the product page for "Sauce Labs Backpack".
6. Click the "Add to Cart" button for the product.
7. Click on the cart icon in the top right corner of the screen.
8. Verify the price and name of the added item in the cart.
9. Initiate the checkout process by clicking "Checkout".
10. Enter the first name.
11. Enter the last name.
12. Enter the zip code.
13. Click "Continue" to proceed with the checkout.
14. Verify that the product name "Sauce Labs Backpack" is displayed in the checkout summary.
15. Complete the order by clicking "Finish".
16. Verify the order completion confirmation message "Thank you for your order!".

**Expected Result:*** The product "Sauce Labs Backpack" is successfully added to the cart.

* The checkout process proceeds smoothly without errors.
* The order is successfully completed, and the user receives the confirmation message "Thank you for your order!".

**Actual Result:*** The product is added to the cart and the checkout process is completed without any issues.

* The user receives the confirmation message "Thank you for your order!" after completing the order.

**Validation Steps:*** Verify that the added product name and price are accurately displayed in the cart.

* Verify that all required fields are successfully entered during the checkout process.
* Verify the presence of the product name "Sauce Labs Backpack" in the checkout summary.
* Verify the display of the confirmation message "Thank you for your order!" upon order completion.


### Test Case 2: Negative Testing - Zip Code Field

**Objective:** To verify the behavior of the website/application when alphabetic characters are entered in the zip code field.**Precondition:**1. The website/application is accessible.

1. The zip code field is present on the relevant form.

**Test Data:*** Username: standard\_user

* Password: [password]
* Product: "Sauce Labs Backpack"

**Test Steps:**1. Launch the browser and navigate to the URL '[https://www.saucedemo.com/](https://www.saucedemo.com/)'.

1. Enter the username as "standard\_user".
2. Enter the password.
3. Click the "Login" button.
4. Navigate to the product page for "Sauce Labs Backpack".
5. Click the "Add to Cart" button for the product.
6. Click on the cart icon in the top right corner of the screen.
7. Initiate the checkout process.
8. Enter the first name.
9. Enter the last name.
10. Enter alphabetic characters in the zip code field instead of numeric values.
11. Attempt to proceed further within the checkout process.

**Expected Result:*** The  website should display a clear and specific error message indicating  that only numeric values are accepted in the zip code field.

* The form should prevent progression to the next step until a valid zip code (numeric input) is provided.

**Actual Result:*** The website should not allow progression and should display appropriate validation for the incorrect zip code field.

**Validation Steps:*** Verify that the system displays a clear and specific error message related to the invalid zip code format.

* Verify that the form prevents progression to the next step until a valid zip code (numeric input) is provided.
