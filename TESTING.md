# TESTING

This document covers all testing completed for **Local Candle Co**, including:

- Manual feature testing  
- User story testing  
- Form validation  
- Authentication & authorization  
- Cart, quantity and checkout testing  
- Email confirmation  
- CRUD testing (FAQ)  
- Lighthouse accessibility  
- HTML, CSS, Python/Pep8 validation  
- Browser/device testing  
- Bugs and fixes  

---

## 1. Manual Feature Testing

All manual tests were completed using:

- Chrome (desktop + mobile)
- Firefox
- Safari (mobile)
- Django development server

---

## 1.1 Navigation Bar

| Test | Expected Result | Pass |
|------|------------------|------|
| Navbar loads on all pages | Visible & styled | ✔️ |
| Mobile shows burger dropdown | Dropdown opens from right | ✔️ |
| Logged-out links show: Login, Register | Correct visibility | ✔️ |
| Logged-in links show: Wishlist, Logout | Correct visibility | ✔️ |
| Cart button always visible | Works & redirects | ✔️ |

---

## 1.2 Product List Page

| Test | Result |
|------|--------|
| Products display in cards | ✔️ PASS |
| View button correctly sized | ✔️ PASS |
| Cards respond to hover | ✔️ PASS |
| Images load correctly | ✔️ PASS |

---

## 1.3 Product Detail Page

| Test | Result |
|------|--------|
| Product image loads | ✔️ PASS |
| Quantity selector appears | ✔️ PASS |
| Add to Cart adds correct qty | ✔️ PASS |
| Wishlist button visible | ✔️ PASS |

---

## 1.4 Wishlist

| Test | Result |
|------|--------|
| Add to wishlist (auth only) | ✔️ PASS |
| Remove from wishlist | ✔️ PASS |
| Wishlist page shows correct items | ✔️ PASS |
| Unauthorized users redirected to login | ✔️ PASS |

---

## 1.5 Cart & Quantity Updates

| Test | Result |
|------|--------|
| Add to cart with quantity | ✔️ PASS |
| Cart displays line totals | ✔️ PASS |
| Cart shows quantity update form | ✔️ PASS |
| Update quantity changes totals | ✔️ PASS |
| Removing an item works | ✔️ PASS |
| Cart clears after checkout | ✔️ PASS |

---

## 1.6 Checkout

| Test | Result |
|------|--------|
| Checkout form validates | ✔️ PASS |
| Stripe PaymentIntent created | ✔️ PASS |
| Order saved as "paid" | ✔️ PASS |
| Success page shown | ✔️ PASS |
| Empty cart redirects to home | ✔️ PASS |

---

## 1.7 Order Confirmation Email

### Steps
| Test Area         | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| **Feature**       | Order confirmation email                                           |
| **Location**      | `checkout/views.py` (inside `checkout_view`)                       |
| **Type**          | Manual test                                                        |
| **Email Backend** | Console backend (`django.core.mail.backends.console.EmailBackend`) |

### Test Steps:
1. Start the development server:
- python3 manage.py runserver
2. Open the site in the browser:
- http://127.0.0.1:8000/
3. Add a product to the cart (any candle).
4. Go to the cart page and click Proceed to Checkout.
5. Complete the checkout form with a valid email (e.g. test@example.com).
6. Submit the form to trigger order creation.
7. Observe the Django development server terminal window.

### Expected Result:
- The checkout completes successfully.

- The order is saved in the database with:

    - Total amount

    - Stripe payment ID

    - Name, email, address

    - status = 'paid'

- A confirmation email is printed in the terminal.

### Example console output:
Subject: Your Local Candle Co order
From: Local Candle Co <no-reply@localcandleco.test>
To: test@example.com

Hi Test User,

Thank you for your order from Local Candle Co.
Order ID: 12
Total: R189.00

We’re getting your candles ready and will email you when they ship.

Warm regards,
Local Candle Co


### Pass / Fail

| Test | Result |
|------|--------|
| Email is printed in terminal | ✔️ PASS |
| Checkout completes | ✔️ PASS |
| No exceptions occur | ✔️ PASS |
| Email content matches expected | ✔️ PASS |

---

## 1.8 FAQ CRUD (Admin Only)

| Test | Result |
|------|--------|
| FAQ list visible to admin | ✔️ PASS |
| Add FAQ works | ✔️ PASS |
| Edit FAQ updates values | ✔️ PASS |
| Delete FAQ removes item | ✔️ PASS |
| Public FAQ page shows only published items | ✔️ PASS |
| Non-admin redirects if attempting CRUD | ✔️ PASS |

---

## 2. User Story Testing

| User Story | Result |
|------------|--------|
| Browse all candles | ✔️ PASS |
| View detail page | ✔️ PASS |
| Add to cart | ✔️ PASS |
| View cart & checkout | ✔️ PASS |
| Register/login/logout | ✔️ PASS |
| Wishlist features | ✔️ PASS |
| Admin manage products | ✔️ PASS |
| Admin manage FAQs | ✔️ PASS |

---

## 3. Form Validation

| Form | Behaviour | Result |
|-------|-------------|---------|
| Contact form | Shows errors for empty/invalid | ✔️ PASS |
| Newsletter form | Validates email | ✔️ PASS |
| Checkout form | All fields required | ✔️ PASS |
| FAQ form | Admin-only, validates fields | ✔️ PASS |

---

## 4. Authentication & Authorization

| Test | Result |
|------|--------|
| Anonymous cannot access FAQ CRUD | ✔️ PASS |
| Wishlist requires login | ✔️ PASS |
| Checkout allowed for anonymous | ✔️ PASS |
| Admin panel access restricted | ✔️ PASS |

---

## 5. Lighthouse Accessibility Tests

| Page | Score | Notes |
|-------|--------|---------|
| Home | 95–100 | ✔️ Good contrast & landmarks |
| Product detail | 90+ | ✔️ Simple structure |
| Cart | 100 | ✔️ |
| FAQ | 100 | ✔️ |

---

## 6. Validator Testing

### 6.1 HTML

HTML validated using browser DevTools → No critical errors.

### 6.2 CSS

Validated via https://jigsaw.w3.org/css-validator/  
✔️ No major issues  
✔️ Minor vendor-prefix warnings ignored

### 6.3 Python (PEP8)

Used `autopep8` and VS Code formatting  
✔️ All files formatted  
✔️ No major warnings

---

## 7. Browser & Device Testing

| Device/Browser | Result |
|----------------|--------|
| Chrome Desktop | ✔️ PASS |
| Chrome Mobile Simulator | ✔️ PASS |
| Firefox | ✔️ PASS |
| Safari/iPhone | ✔️ PASS |
| Edge | ✔️ PASS |

---

## 8. Known Bugs & Fixes

### Fixed
- Navbar not collapsing on mobile → replaced with dropdown burger
- Product cards misaligned → improved flexbox structure
- Quantity update not working → added `cart_update` view
- FAQ CRUD missing → implemented full admin CRUD

### Remaining (Optional)
- AJAX “add to cart” (non-essential)
- Real email backend (optional upgrade)

---

## 9. Final Result

All core functionality has passed testing and meets:  
- LO1 (e-commerce + Stripe)  
- LO2 (UX + testing)  
- LO3 (SEO)  
- LO4 (auth)  
- LO5 (marketing)  
- LO6 (e-commerce fundamentals)

✔️ **All Must-Have features working**  
✔️ Should-Have features mostly completed  
✔️ Project ready for final deployment & polishing  