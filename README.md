# 🧩 Simple Serverless URL Shortener

A minimal URL shortener built using:
- **AWS Lambda** (Python backend)
- **DynamoDB** (URL storage)
- **S3 Static Website Hosting** (Frontend)

---

## 🖼 Live Demo

Visit the deployed frontend here:  
🔗 http://url-shortener-yarden.s3-website-us-west-2.amazonaws.com

---

## 🔧 Files

- `index.html`: The frontend (you already have this).
- `lambda_function.py`: Lambda code to shorten and redirect.
- `README.md`: This file.

---

## 📦 AWS Components

### 1. DynamoDB
- Table name: `ShortUrls`
- Primary key: `id` (string)
- Attributes:
  - `id`: short code
  - `url`: original URL

### 2. Lambda Function
- Runtime: Python 3.x
- Permissions: DynamoDB full access
- Endpoint: Lambda Function URL (enable in console)
- Handler: `lambda_function.lambda_handler`

### 3. S3 Static Website
- Bucket: Public, static hosting enabled
- Upload `index.html`
- Replace JS fetch URL with your Lambda URL

---

## 💡 Usage

- User enters long URL in input field.
- JS sends POST to Lambda Function: `/shorten`
- Lambda generates short ID and stores in DynamoDB.
- When user visits `/short_id`, the Lambda GET handler redirects.

---

## 🧪 Testing

- Shorten:  
  `POST /shorten` with JSON: `{ "url": "https://example.com" }`  
  Returns: `{ "id": "abc123" }`

- Redirect:  
  `GET /abc123` → Redirects to stored long URL.

---

## 📁 How to Deploy

1. Upload `index.html` to S3 and enable static site hosting.
2. Create DynamoDB table named `ShortUrls`.
3. Deploy Lambda function using `lambda_function.py`.
4. Update `index.html` to point to your Lambda Function URL.

---

✅ That's it! You now have a fully working, serverless URL shortener.
