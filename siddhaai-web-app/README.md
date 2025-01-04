# Nuxt Project

This is a Nuxt project. To start the project, follow these steps:
Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

1. Install Node.js and npm.
2. Clone the repository.
3. Install the dependencies.
4. Run the development server.

## Install Node.js and npm

You can install Node.js and npm from the [official website](https://nodejs.org/en/).

## Clone the repository

`https://github.com/bhaaratkrishnan/siddhai-demo-nuxt.git`

## Install the dependencies

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install
```

## Development Server

Start the development server on `http://localhost:3000` using the command:

```bash
npm run dev
```

## Production

Build the application for production:

```bash
npm run build
```

Locally preview production build:

```bash
npm run preview
```

# Docker Development

1. Install docker and docker-compose.
2. Clone this repository.

## Command:
The given command starts the docker container for node, nuxt environment with neccessary port forwarding. 
The development server start in `localhost:3000`
### Normal Mode:
```bash
docker-compose up
```

### Detached Mode:
```bash
docker-compose up -d
```

### Closing the containers
```bash 
docker-compose down
```


## Guildlines 

### Folders 
1. `assets` - The assets folder in Nuxt is a special directory that is used to store uncompiled assets, such as images, fonts, and Stylus or Sass files.
2. `components` - The components folder in Nuxt is where you put all of your Vue.js components. Components are what make up the different parts of your page and can be reused and imported into your pages, layouts, and even other components.
3. `layouts` - The layouts folder in Nuxt is a special directory where you can store your application's layouts. Layouts are reusable components that can be used to define the overall structure of your pages.  
4. `pages` - The pages folder in Nuxt is where you define your application's pages. Each page is a Vue component that can be accessed by a URL. The pages folder is a required directory in Nuxt projects.

### [Components and Pages Guildlines](guildlines.md)