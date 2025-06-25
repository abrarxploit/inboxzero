from inboxzero.purge_engine import purge_inbox


def main():
    print("📬 Running InboxZero CLI Purge Engine...\n")
    results = purge_inbox()

    print("\n✅ Summary:")
    print(f"Kept Emails   : {len(results['kept'])}")
    print(f"Deleted Emails: {len(results['deleted'])}")

if __name__ == "__main__":
    main()
