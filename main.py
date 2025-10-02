import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    topic = "AIで稼ぐ方法（初心者向け）"
    prompt = f"{topic} についてブログ記事を書いてください。"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response["choices"][0]["message"]["content"]

    with open("article.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ 記事生成完了！article.txt に保存しました")

if __name__ == "__main__":
    main()
