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
