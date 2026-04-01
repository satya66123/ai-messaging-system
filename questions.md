# Interview Questions & Answers

## 1. What is this project about?

This is an AI-driven automation system that reads emails, processes them using rule-based logic, generates responses using an LLM, and optionally sends replies via WhatsApp.

---

## 2. Why did you build this project?

To demonstrate real-world AI integration with APIs, automation workflows, and backend systems.

---

## 3. What challenges did you face?

* OAuth authentication issues
* API security restrictions
* Handling sensitive data
* Designing rule-based filtering
* Debugging third-party integrations

---

## 4. How did you handle secrets?

Used `.env` file and removed sensitive data from Git history.

---

## 5. How does your rule engine work?

It filters emails into:

* Critical (security alerts)
* Important (work-related)
* Ignored (spam/system)

---

## 6. Why use FastAPI?

FastAPI provides high performance, async support, and easy API development.

---

## 7. How does AI integration work?

The system sends email content to an LLM (Ollama) and gets a context-aware response.

---

## 8. How did you ensure safe AI responses?

By designing strict prompts and avoiding assumptions in generated replies.

---

## 9. What improvements would you make?

* Add database storage
* Deploy on cloud
* Add authentication
* Improve UI

---

## 10. Is this production ready?

Core system is production-capable, but needs scaling, monitoring, and security enhancements.
