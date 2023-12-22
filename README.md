[![codecov](https://codecov.io/gh/One-District-One-Product/ODOP-Dev/branch/main/graph/badge.svg)](https://codecov.io/gh/One-District-One-Product/ODOP-Dev)

## One District One  Product
The One District One Product (ODOP) initiative is a unique program designed to promote the distinctive products that each district of Jammu and Kashmir excels in. It aims to support local artisans and producers, uplift local economies, and preserve traditional craftsmanship.

In our specific implementation of the ODOP project, the primary objective of the platform is to cut out intermediaries from the supply chain, enabling producers to receive fair remuneration for their products while giving consumers access to a diverse range of authentic ODOP items.

## Getting Started
To get started with our ODOP project, you don't need to install any software. It's an online platform that can be accessed from your web browser.

## Prerequisites
The ODOP project is accessible through a web browser, so you only need an internet connection to get started. There are no specific software or hardware prerequisites for using the project.

## Installation

As mentioned earlier, there's no installation required for our ODOP project. It is a web-based platform, and you can access it directly by visiting project website.

## Usage/Examples

Producers POV:
1. Visit the official odop website.
2. Register themselves on the website.
3. Complete authentication by providing their unique agricultural license number.
4. Upload the product images and other relevant details and descriptions like.
5. Finally submit the product and let people know about their unique products.

Consumers POV:
1. Visit the official odop website.
2. Explore the diverse range of ODOP products showcased on the platform.
3. Click on individual product listings to read about the artisans who create them, their stories, and the unique characteristics of each products.


```npm start```
```npm test```
```npm run build```

##Screenshots

![WhatsApp Image 2023-10-19 at 9 03 17 AM](https://github.com/One-District-One-Product/ODOP-Dev/assets/113474452/fb4967ca-6ed1-4d53-9ec4-0e50f34151d6)

![WhatsApp Image 2023-10-19 at 9 03 11 AM](https://github.com/One-District-One-Product/ODOP-Dev/assets/113474452/80afbd10-6e4e-4f3f-a81b-8103571d8f48)

![WhatsApp Image 2023-10-19 at 9 03 04 AM](https://github.com/One-District-One-Product/ODOP-Dev/assets/113474452/9910186d-37d1-494e-b3f0-93fab497335a)

##Flowcharts

###Producer POV

```mermaid
flowchart TD;
    setup-dev(Identification of unique Products)
    bci(Market Research)
    bci-register(Register Producers on Website)
    bci-auth(Authentication)
    bci-upload(Upload Product Images)
    bci-detail(Fill Product Details)
    bci-submit((Submit))
    setup-dev-->bci
    bci-->bci-register
    bci-register-->bci-auth
    bci-auth-->bci-upload
    bci-upload-->bci-detail
    bci-detail-->bci-submit
```

###Consumer POV

```mermaid
flowchart TD;
    setup-dev(Visit the Website)
    bci(Browse through the districts)
    bci-search(Check out authentic products of each district)
    bci-detail(View product image and detail by various producers)
    bci-compare(Compare the products from different sellers)
    bci-contact(Contact the seller)
    bci-done((Complete))
    setup-dev-->bci
    bci-->bci-search
    bci-search-->bci-detail
    bci-detail-->bci-compare
    bci-compare-->bci-contact
    bci-contact-->bci-done
```

Test Whole pipeline
