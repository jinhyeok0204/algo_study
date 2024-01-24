def main():
    n, m = map(int,input().split())

    num_of_know, *know_persons = map(int, input().split())

    know_persons = set(know_persons)
    lie_persons = set()
    parties = []

    lie_count = 0
    for _ in range(m):
        num_of_attend, *attendees = map(int, input().split())

        no_one_know = True
        for attendee in attendees:
            if attendee in know_persons:
                know_persons += attendees # 합집합

                break
        # 거짓말을 들은 사람이 진실을 듣게 되면 거짓말쟁이가 됨
        # 진실을 들은 사람이 거짓말을 듣게 되도 거짓말쟁이가 됨
        # 진실을 아는 사람이 파티에 있으면 진실을 말해야 함











if __name__ == '__main__':
    main()
