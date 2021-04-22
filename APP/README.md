# P06-Cliente (p06-cliente)

Cliente Android para P06 hecho con Quasar sobre Capacitor

## Install the dependencies
```bash
npm install
```

### Add android mode with capacitor 
Note: it requires android studio installed an configured

```bash
quasar mode add capacitor
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
IMPORTANT: *DO NOT* run any updates on the proyect from android studio or it will break

```bash
# Web mode
quasar dev

# Android mode
quasar dev -m capacitor -T android
```

### Lint the files
```bash
npm run lint
```

### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.conf.js](https://v1.quasar.dev/quasar-cli/quasar-conf-js).
