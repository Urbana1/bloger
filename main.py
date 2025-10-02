import os
import openai

openai.api_key = os.getenv("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")

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
