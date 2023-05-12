#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p7;
	listint_t *pv;

	p7 = list;
	pv = list;
	while (list && p7 && p7->next)
	{
		list = list->next;
		p7 = p7->next->next;

		if (list == p7)
		{
			list = pv;
			pv =  p7;
			while (1)
			{
				p7 = pv;
				while (p7->next != list && p7->next != pv)
				{
					p7 = p7->next;
				}
				if (p7->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
