(() => {
  // Configure only the public n8n webhook URL after the workflow is ready.
  // Never put n8n API keys or other secrets in browser-side code.
  const WEBHOOK_URL = "";
  const form = document.querySelector("[data-order-form]");
  if (!form) return;

  const button = form.querySelector('button[type="submit"]');
  const status = document.querySelector("#checkout-status");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    status.textContent = "";
    status.removeAttribute("data-state");

    if (!form.reportValidity()) return;
    if (!WEBHOOK_URL) {
      status.dataset.state = "error";
      status.textContent = "El formulario está listo, pero falta conectar el webhook de pedidos de n8n. No se envió ningún dato.";
      return;
    }

    const values = new FormData(form);
    const payload = {
      event: "bioteck.order.created",
      product: {
        id: "natural-care-kit",
        name: "Kit Natural Care",
        quantity: 1,
        price: 77000,
        currency: "COP",
      },
      paymentMethod: "cash_on_delivery",
      customer: {
        fullName: values.get("fullName").trim(),
        address: values.get("address").trim(),
        department: values.get("department").trim(),
        city: values.get("city").trim(),
        phone: values.get("phone").trim(),
        email: values.get("email").trim(),
      },
      privacyConsent: values.get("privacyConsent") === "true",
      submittedAt: new Date().toISOString(),
    };

    button.disabled = true;
    button.setAttribute("aria-busy", "true");
    status.textContent = "Registrando tu pedido…";

    try {
      const response = await fetch(WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error("webhook-response");

      form.reset();
      status.dataset.state = "success";
      status.textContent = "Pedido registrado. Abriendo las opciones para confirmar tu compra…";
      window.location.assign("confirmacion.html");
    } catch {
      status.dataset.state = "error";
      status.textContent = "No pudimos registrar el pedido en este momento. Revisa tu conexión o inténtalo de nuevo.";
    } finally {
      button.disabled = false;
      button.removeAttribute("aria-busy");
    }
  });

  // Keep the form inert unless JavaScript is available to prevent a GET submission
  // from placing customer details in the page URL.
  button.disabled = false;
})();
