<p align="center"><img src="logo.png" width="96" alt="Follower Diff logo"></p>

<h1 align="center">Follower Diff</h1>

<p align="center"><b>See who followed and who unfollowed you on Instagram.</b><br>
Private, free, and safe for your account. No Instagram login, no bots, works offline.</p>

<p align="center"><a href="https://samutecyt.github.io/follower-diff/"><b>Open the app</b></a> · <a href="https://github.com/SamuTecYT/follower-diff/releases/latest/download/Follower-Diff.html"><b>Download for PC / Mac</b></a> · <a href="https://samutecyt.github.io/follower-diff/#demo">Try it with example data</a></p>

<p align="center">
  <a href="#español">Español</a> · <a href="#english">English</a>
</p>

<p align="center"><img src="screenshots/desktop-en.png" width="720" alt="Follower Diff on desktop with example data"></p>

<p align="center">
  <img src="screenshots/mobile-es.png" width="230" alt="Phone view in Spanish">
  <img src="screenshots/mobile-ar.png" width="230" alt="Phone view in Arabic">
  <img src="screenshots/mobile-ja.png" width="230" alt="Phone view in Japanese">
</p>

<p align="center"><sub>All screenshots use made-up example data.</sub></p>

---

## English

### Get it
**On a computer (Windows or Mac):**
1. Click **[Download Follower Diff](https://github.com/SamuTecYT/follower-diff/releases/latest/download/Follower-Diff.html)**. You get one file: `Follower-Diff.html`.
2. Double-click it. It opens in your browser and works **without internet**.
3. Optional: drag the file to your desktop so it's always at hand.

**On a phone (iPhone or Android):** open **[the app](https://samutecyt.github.io/follower-diff/)** in Safari or Chrome, tap **Share › Add to Home Screen**. It gets its own icon, like an app.

### Optional account
Protect your history with a password. No server: everything stays encrypted on your device. 100% optional.

- **Create it:** tap **Create account**, type a nickname and a password. Done.
- **Use it on another device (3 steps):**
  1. Tap **Move to another device**. You get `follower-account.json`.
  2. Send it to yourself (WhatsApp, email, AirDrop or Drive). It's encrypted.
  3. On the other device tap **I have an account**, choose the file and type your password.
- **Important:** devices don't update by themselves. **Every time** you add a new Instagram file and want to see it on your other device, tap **Move to another device** again and load the new file there.
- If you forget the password it can't be recovered, because no one else has it.

### What it does
Instagram lets you download your own data, including your list of followers. Follower Diff takes that file and compares it with the previous one, so you can see:

- **Who started following you** since last time
- **Who unfollowed you** since last time
- **Followed you again**: if someone unfollows you and later follows you again, the app tells you, with Instagram's date (it even notices when they left and came back between two files)
- **Accounts that show up again**: if Instagram left someone out of an earlier file, the app uses Instagram's own follow date to list them apart instead of calling them new
- **Who you follow that doesn't follow you back**
- **Who follows you that you don't follow back**
- **Mutual follows**: everyone you follow who also follows you
- **Search any user** to see at once if you follow each other, only one way, or not at all. All lists filter as you type
- Built for **big accounts**: tested with 100,000 followers. Long lists load in pages, so the app stays fast
- Tap a name to open the profile: **in the Instagram app** on phones, in your default browser on computers
- **Copy any list** with one tap
- **Dark mode** that follows your device
- A **history** of every snapshot, with follower counts and dates

### Why it can't get you banned
It uses only Instagram's official **Download your information** feature. The app never logs into your account, never asks for your password, and doesn't automate anything on Instagram.

### Privacy and security
- **Nothing leaves your device.** The page has a strict Content Security Policy that blocks every network connection, so your followers can't be sent anywhere.
- **No servers, no tracking, no cookies, no analytics.** The optional account is not online: it's a password that encrypts your history on your own device (AES-256).
- Usernames read from the file are checked against Instagram's username rules before they are shown. A tampered file can't inject code.
- History is stored only in your browser. You can save a backup and load it later (encrypted if you have an account).
- A single, readable HTML file with no dependencies. You can audit all of it.

### How to use
1. Open **https://samutecyt.github.io/follower-diff/** (or the downloaded `Follower-Diff.html`) in any modern browser, on a computer or a phone.
2. Request your file, whichever way you prefer:
   - **On the web:** tap **Request my file from Instagram**. It opens the export screen directly.
   - **In the Instagram app** (no sign-in needed): Profile › ≡ › Accounts Center › Your information and permissions › Export your information.

   Then: **Create export** › your account › **Export to device** › *Customize information*: only **Followers and following** (in the *Connections* section) › Date range: **All time** › **Start export**. Leave everything else as it is: the format doesn't matter (HTML or JSON both work).
3. Wait until it's ready: it usually takes about **30 seconds**, but sometimes Instagram takes longer (minutes or hours). That's normal, don't request it again. The screen doesn't refresh by itself: close **Export your information**, open it again and tap **Download**.
4. Download the `.zip` and drop it into the page **without unzipping it**.
5. Repeat whenever your follower count changes. Each new file is compared with the previous one.

### Languages
Opens in your device's language automatically, and you can switch at any time from the selector at the top:
English, Español, Português, Français, Deutsch, Italiano, Русский, Türkçe, العربية (right-to-left), हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia.

---

## Español

### Descargarlo
**En el ordenador (Windows o Mac):**
1. Pulsa **[Descargar Follower Diff](https://github.com/SamuTecYT/follower-diff/releases/latest/download/Follower-Diff.html)**. Se baja un único archivo: `Follower-Diff.html`.
2. Haz doble clic en él. Se abre en tu navegador y funciona **sin internet**.
3. Si quieres, arrástralo al escritorio para tenerlo siempre a mano.

**En el móvil (iPhone o Android):** abre **[la app](https://samutecyt.github.io/follower-diff/)** en Safari o Chrome y pulsa **Compartir › Añadir a pantalla de inicio**. Tendrá su propio icono, como una app.

### Cuenta opcional
Protege tu historial con una contraseña. Sin servidor: todo queda cifrado en tu aparato. 100 % opcional.

- **Crearla:** pulsa **Crear cuenta**, escribe un apodo y una contraseña. Listo.
- **Usarla en otro aparato (3 pasos):**
  1. Pulsa **Pasar a otro aparato**. Se descarga `follower-account.json`.
  2. Envíatelo (WhatsApp, correo, AirDrop o Drive). Va cifrado.
  3. En el otro aparato pulsa **Ya tengo cuenta**, elige el archivo y escribe tu contraseña.
- **Importante:** los aparatos no se actualizan solos. **Cada vez** que subas un archivo nuevo de Instagram y quieras verlo en tu otro aparato, vuelve a pulsar **Pasar a otro aparato** y carga el archivo nuevo allí.
- Si olvidas la contraseña no se puede recuperar, porque nadie más la tiene.

### Qué hace
Instagram te deja descargar tus propios datos, incluida tu lista de seguidores. Follower Diff compara ese archivo con el anterior y te muestra:

- **Quién te empezó a seguir** desde la última vez
- **Quién te dejó de seguir**
- **Te volvieron a seguir**: si alguien te deja de seguir y luego vuelve, el programa te avisa, con la fecha de Instagram (lo nota incluso si se fue y volvió entre dos archivos)
- **Cuentas que vuelven a aparecer**: si Instagram dejó a alguien fuera de un archivo anterior, el programa usa la fecha de Instagram para separarlo en vez de decir que es nuevo
- **A quién sigues y no te sigue**
- **Quién te sigue y tú no le sigues**
- **Seguidores mutuos**: quién te sigue y tú también le sigues
- **Busca cualquier usuario** y ve al momento si os seguís, si solo te sigue uno de los dos o ninguno. Todas las listas se filtran mientras escribes
- Pensado para **cuentas grandes**: probado con 100.000 seguidores. Las listas largas se cargan por partes para que todo vaya rápido
- Toca un nombre para abrir su perfil: **en la app de Instagram** en el móvil y en tu navegador predeterminado en el ordenador
- **Copia cualquier lista** con un toque
- **Modo oscuro** automático según tu aparato
- Un **historial** con cada registro, su fecha y el número de seguidores

### Por qué no te pueden banear
Solo usa la función oficial **Descargar tu información** de Instagram. La app nunca entra a tu cuenta, no pide contraseñas y no automatiza nada en Instagram.

### Privacidad y seguridad
- **Nada sale de tu aparato.** La página bloquea cualquier conexión a internet, así que tus seguidores no pueden enviarse a ningún sitio.
- **Sin servidores, sin rastreo, sin cookies.** La cuenta opcional no está en internet: es una contraseña que cifra tu historial en tu propio aparato (AES-256).
- Los nombres del archivo se validan antes de mostrarse. Un archivo manipulado no puede meter código.
- El historial se guarda solo en tu navegador. Puedes guardar una copia y cargarla después (cifrada si tienes cuenta).
- Es un único archivo HTML, sin dependencias, que cualquiera puede revisar.

### Cómo usarlo
1. Abre **https://samutecyt.github.io/follower-diff/** (o el `Follower-Diff.html` descargado) en cualquier navegador moderno, en el ordenador o en el móvil.
2. Pide tu archivo como prefieras:
   - **En la web:** toca **Pedir mi archivo a Instagram**. Te lleva directo a la pantalla de exportación.
   - **En la app de Instagram** (sin iniciar sesión): Perfil › ≡ › Centro de cuentas › Tu información y permisos › Exportar tu información.

   Después: **Crear exportación** › tu cuenta › **Exportar a dispositivo** › *Personalizar información*: solo **Seguidores y seguidos** (en el apartado *Conexiones*) › Intervalo de fechas: **Desde el principio** › **Iniciar exportación**. Lo demás déjalo como esté: el formato da igual (sirve HTML o JSON).
3. Espera a que esté listo: suele tardar unos **30 segundos**, pero a veces Instagram tarda más (minutos u horas). Es normal, no lo pidas otra vez. La pantalla no se actualiza sola: cierra **Exportar tu información**, vuelve a entrar y toca **Descargar**.
4. Descarga el `.zip` y súbelo a la página **sin descomprimirlo**.
5. Repite cuando cambie tu número de seguidores. Cada archivo se compara con el anterior.

### Idiomas
Se abre solo en el idioma de tu aparato y puedes cambiarlo cuando quieras desde el selector de arriba:
English, Español, Português, Français, Deutsch, Italiano, Русский, Türkçe, العربية (de derecha a izquierda), हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia.

---

## What's new / Novedades (v3.0)
- **Floating guide on phones**: tap *Turn on floating guide* and the steps stay on top of Instagram in a small window (picture-in-picture), so you don't have to switch back and forth. Choose its shape (tall, square or wide) and the text resizes itself to fit; pinch it to make it bigger. It's a short video made inside your phone; nothing is sent anywhere · **Guía flotante en el móvil**: toca *Activar guía flotante* y los pasos se quedan encima de Instagram en una ventanita (imagen en imagen), sin ir y volver. Elige su forma (alta, cuadrada o ancha) y el texto se ajusta solo; pellízcala para agrandarla. Es un vídeo corto hecho dentro de tu teléfono; no se envía nada
- Clearer **In the app** tab: tab icons, stronger selected state in light and dark, drawn menu icon, the 2 steps to change highlighted · Pestaña **En la app** más clara: iconos en las pestañas, selección más visible en claro y oscuro, icono del menú dibujado, los 2 pasos a cambiar resaltados
- **One clear guide in 3 steps** (request · download · upload) instead of two separate lists · **Una sola guía clara en 3 pasos** (pedir · descargar · subir) en lugar de dos listas separadas
- **On the web / In the app tabs**, each with its own step-by-step, now visible on computers too; phones open on "In the app" · **Pestañas «En la web» / «En la app»**, cada una con su paso a paso, ahora también visibles en el ordenador; en el móvil se abre en «En la app»
- The 2 settings you must change are marked **Change this** · Las 2 opciones que hay que cambiar llevan la marca **Cambia esto**
- Step 2 names the exact screen and button; tidier phone header; version shown in the footer; arrows mirrored in Arabic · El paso 2 nombra la pantalla y el botón exactos; cabecera del móvil más ordenada; versión visible al pie; flechas invertidas en árabe

## v2.9
- **One step fewer**: no need to change the format anymore; the app reads both HTML (Instagram's default) and JSON. Only 2 settings to change: "Followers and following" and "All time" · **Un paso menos**: ya no hace falta cambiar el formato; el programa lee HTML (lo que trae Instagram por defecto) y JSON. Solo cambias 2 cosas: «Seguidores y seguidos» y «Desde el principio»

## v2.8
- **"What to tap" list** right under the request buttons: the 3 exact steps on Instagram's export screen, always visible (Instagram doesn't allow any link to pre-tick the options) · Lista **«Qué tocar»** justo debajo de los botones: los 3 pasos exactos en la pantalla de exportación de Instagram, siempre a la vista (Instagram no permite que un enlace deje las opciones marcadas)

## v2.7
- Clearer **Step 1** card: request your file **on the web** (takes you straight there) or **in the Instagram app** (no sign-in needed), with a note on why signing in is safe · Tarjeta **Paso 1** más clara: pide tu archivo **desde la web** (te lleva directo) o **desde la app de Instagram** (sin iniciar sesión), con una nota de por qué iniciar sesión es seguro

## v2.6
- **Light / dark mode button** next to the language selector · Botón de **modo claro / oscuro** junto al idioma
- On phones, **Open the Instagram app** button (you're already signed in there) plus the exact path to the export · En el móvil, botón **Abrir la app de Instagram** (ya tienes la sesión iniciada) y la ruta exacta para pedir el archivo

## v2.5
- Optional **account** with password, encrypted on your device · **Cuenta** opcional con contraseña, cifrada en tu aparato
- **I have an account** / **Move to another device** in 3 steps · **Ya tengo cuenta** / **Pasar a otro aparato** en 3 pasos
- Search, mutual follows, copy lists, dark mode, big-account support · Buscador, mutuos, copiar listas, modo oscuro, cuentas grandes
- Profiles open in the Instagram app on phones · Los perfiles se abren en la app de Instagram en el móvil

## For developers
- `src/app.html`: the source (HTML, CSS, JS and all translations in one file)
- `build.py`: embeds the logo and writes `index.html` (requires Python and Pillow)
- Try it with example data by opening `index.html#demo` (or `#demo-ja`, `#demo-ar`, …)

## Credits and license / Créditos y licencia
Created by **[SamuTecYT](https://github.com/SamuTecYT)**. Free to use, copy and modify under the [MIT License](LICENSE), **as long as you credit the creator** and keep the license notice.

Creado por **SamuTecYT**. Puedes usarlo, copiarlo y modificarlo gratis con la licencia MIT, **siempre que des crédito a su creador** y mantengas el aviso de licencia.

## Disclaimer / Aviso legal
Independent project, not affiliated with, endorsed by or connected to Instagram or Meta Platforms, Inc. Provided "as is", without warranty of any kind. Each user is responsible for how they use it. The creator is not liable for any damage, data loss or consequence to any account.

Proyecto independiente, sin relación con Instagram ni Meta. Se ofrece "tal cual", sin garantías. Cada persona es responsable del uso que le dé y el creador no se hace responsable de ningún daño, pérdida de datos o consecuencia en ninguna cuenta.
