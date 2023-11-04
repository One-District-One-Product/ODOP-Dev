## One District One Product
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

![image]()<img width="1470" alt="Screenshot 2023-10-19 at 9 02 45 AM" src="https://github.com/One-District-One-Product/odop-frontend/assets/127433098/4470a6e1-14be-4123-a930-2f1285fcfa1a">

![image]()<img width="1470" alt="Screenshot 2023-10-19 at 9 02 26 AM" src="https://github.com/One-District-One-Product/odop-frontend/assets/127433098/fc47efd1-a35c-4119-a3e0-43379f7e8c10">

<img width="1470" alt="Screenshot 2023-10-19 at 9 02 16 AM" src="https://github.com/One-District-One-Product/odop-frontend/assets/127433098/fcc6ef65-6c94-46e8-a20b-31378591d50d">

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
    bci-end((Complete))
    setup-dev-->bci
    bci-->bci-search
    bci-search-->bci-detail
    bci-detail-->bci-compare
    bci-compare-->bci-contact
    bci-contact-->bci-end
```
