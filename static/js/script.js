<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', () => {
    // --- 1. LÓGICA DE BÚSQUEDA ---
    const inputBuscador = document.getElementById('buscadorProyectos');
    const seccionCategorias = document.getElementById('seccionCategorias');
    const seccionResultados = document.getElementById('seccionResultados');
    const tarjetasProyectos = document.querySelectorAll('.tarjeta-proyecto-wrapper');
    const contadorResultados = document.getElementById('contadorResultados');
    const mensajeSinResultados = document.getElementById('mensajeSinResultados');

    if (inputBuscador) {
        inputBuscador.addEventListener('input', (e) => {
            const termino = e.target.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();

            if (termino.length > 0) {
                if (seccionCategorias) seccionCategorias.classList.add('d-none');
                if (seccionResultados) seccionResultados.classList.remove('d-none');

                let coincidenciaContador = 0;

                tarjetasProyectos.forEach(tarjeta => {
                    const textoTarjeta = tarjeta.innerText.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

                    if (textoTarjeta.includes(termino)) {
                        tarjeta.classList.remove('d-none');
                        coincidenciaContador++;
                    } else {
                        tarjeta.classList.add('d-none');
                    }
                });

                if (contadorResultados) {
                    contadorResultados.textContent = `${coincidenciaContador} proyecto${coincidenciaContador !== 1 ? 's' : ''}`;
                }

                if (mensajeSinResultados) {
                    if (coincidenciaContador === 0) {
                        mensajeSinResultados.classList.remove('d-none');
                    } else {
                        mensajeSinResultados.classList.add('d-none');
                    }
                }
            } else {
                if (seccionCategorias) seccionCategorias.classList.remove('d-none');
                if (seccionResultados) seccionResultados.classList.add('d-none');
            }
        });
    }

    // --- 2. CUENTA REGRESIVA (28 OCTUBRE 2026) ---
    const fechaEvento = new Date('October 28, 2026 09:00:00').getTime();

    function actualizarCuentaRegresiva() {
        const ahora = new Date().getTime();
        const diferencia = fechaEvento - ahora;

        if (diferencia > 0) {
            const d = Math.floor(diferencia / (1000 * 60 * 60 * 24));
            const h = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diferencia % (1000 * 60)) / 1000);

            if (document.getElementById('dias')) document.getElementById('dias').innerText = d < 10 ? '0' + d : d;
            if (document.getElementById('horas')) document.getElementById('horas').innerText = h < 10 ? '0' + h : h;
            if (document.getElementById('minutos')) document.getElementById('minutos').innerText = m < 10 ? '0' + m : m;
            if (document.getElementById('segundos')) document.getElementById('segundos').innerText = s < 10 ? '0' + s : s;
        }
    }

    actualizarCuentaRegresiva();
    setInterval(actualizarCuentaRegresiva, 1000);
=======
document.addEventListener('DOMContentLoaded', () => {
    // --- 1. LÓGICA DE BÚSQUEDA ---
    const inputBuscador = document.getElementById('buscadorProyectos');
    const seccionCategorias = document.getElementById('seccionCategorias');
    const seccionResultados = document.getElementById('seccionResultados');
    const tarjetasProyectos = document.querySelectorAll('.tarjeta-proyecto-wrapper');
    const contadorResultados = document.getElementById('contadorResultados');
    const mensajeSinResultados = document.getElementById('mensajeSinResultados');

    if (inputBuscador) {
        inputBuscador.addEventListener('input', (e) => {
            const termino = e.target.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();

            if (termino.length > 0) {
                if (seccionCategorias) seccionCategorias.classList.add('d-none');
                if (seccionResultados) seccionResultados.classList.remove('d-none');

                let coincidenciaContador = 0;

                tarjetasProyectos.forEach(tarjeta => {
                    const textoTarjeta = tarjeta.innerText.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

                    if (textoTarjeta.includes(termino)) {
                        tarjeta.classList.remove('d-none');
                        coincidenciaContador++;
                    } else {
                        tarjeta.classList.add('d-none');
                    }
                });

                if (contadorResultados) {
                    contadorResultados.textContent = `${coincidenciaContador} proyecto${coincidenciaContador !== 1 ? 's' : ''}`;
                }

                if (mensajeSinResultados) {
                    if (coincidenciaContador === 0) {
                        mensajeSinResultados.classList.remove('d-none');
                    } else {
                        mensajeSinResultados.classList.add('d-none');
                    }
                }
            } else {
                if (seccionCategorias) seccionCategorias.classList.remove('d-none');
                if (seccionResultados) seccionResultados.classList.add('d-none');
            }
        });
    }

    // --- 2. CUENTA REGRESIVA (28 OCTUBRE 2026) ---
    const fechaEvento = new Date('October 28, 2026 09:00:00').getTime();

    function actualizarCuentaRegresiva() {
        const ahora = new Date().getTime();
        const diferencia = fechaEvento - ahora;

        if (diferencia > 0) {
            const d = Math.floor(diferencia / (1000 * 60 * 60 * 24));
            const h = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diferencia % (1000 * 60)) / 1000);

            if (document.getElementById('dias')) document.getElementById('dias').innerText = d < 10 ? '0' + d : d;
            if (document.getElementById('horas')) document.getElementById('horas').innerText = h < 10 ? '0' + h : h;
            if (document.getElementById('minutos')) document.getElementById('minutos').innerText = m < 10 ? '0' + m : m;
            if (document.getElementById('segundos')) document.getElementById('segundos').innerText = s < 10 ? '0' + s : s;
        }
    }

    actualizarCuentaRegresiva();
    setInterval(actualizarCuentaRegresiva, 1000);
>>>>>>> 4e958ecdf266c3cb32c59a4e10ac2a7d98e3b4c4
});